import streamlit as st
import random
import string
import json
from huggingface_hub import InferenceClient
import requests

# ----------------- Page Config ------------------
st.set_page_config(page_title="AI Toolkit", page_icon="🎲", layout="centered")

# ----------------- Sidebar ------------------
st.sidebar.title("🧰 Tools")
tool = st.sidebar.radio(
    "Choose a Tool", 
    ["Random Name Generator", "Random Password Generator", "LLaMA 3.1 Chatbot", "Text to Image Generator"]
)

st.sidebar.markdown("---")
st.sidebar.info("Empowering people through open-source innovation.")

# ----------------- Load Names from JSON ------------------
@st.cache_data
def load_names():
    with open("random_names.json", "r") as f:
        return json.load(f)

names = load_names()

# ----------------- Utility Functions ------------------
def generate_random_name():
    person = random.choice(names)
    return f"{person['first_name']} {person['last_name']}"

def generate_random_password(length=12, mode="All"):
    if mode == "Letters Only":
        chars = string.ascii_letters
    elif mode == "Numbers Only":
        chars = string.digits
    elif mode == "Letters + Numbers":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

# ----------------- Hugging Face Token ------------------
HF_TOKEN = st.secrets["HF_TOKEN"]

# ----------------- Hugging Face Clients ------------------
# Text-to-Image client
image_client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN,
)

# Chatbot
def query_llama3(question):
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Text-to-Image (updated)
def text_to_image(prompt):
    try:
        image = image_client.text_to_image(
            prompt,
            model="stabilityai/stable-diffusion-3.5-large"
        )
        return image
    except Exception as e:
        st.error(f"Failed to generate image: {e}")
        return None

# ----------------- Main UI ------------------
st.title("AI Master Toolkit")

if tool == "Random Name Generator":
    st.subheader("📛 Random Name Generator")
    if st.button("Generate Name"):
        st.success(f"Generated Name: `{generate_random_name()}`")

elif tool == "Random Password Generator":
    st.subheader("🔑 Random Password Generator")
    length = st.slider("Password Length", 8, 32, 12)
    mode = st.selectbox("Password Type", ["Letters Only", "Numbers Only", "Letters + Numbers", "All"])
    if st.button("Generate Password"):
        password = generate_random_password(length, mode)
        st.success(f"Generated Password: `{password}`")
        st.caption("Keep it secure 🔐")

elif tool == "LLaMA 3.1 Chatbot":
    st.subheader("🤖 Chat with LLaMA 3.1 (Hugging Face)")
    user_input = st.text_input("Ask something...")
    if user_input:
        with st.spinner("Thinking..."):
            response = query_llama3(user_input)
            st.success(response)

elif tool == "Text to Image Generator":
    st.subheader("🎨 Text to Image Generator")
    prompt = st.text_area("Enter your prompt for the image...")
    if st.button("Generate Image"):
        if prompt.strip():
            with st.spinner("Generating image..."):
                image = text_to_image(prompt)
                if image:
                    st.image(image, caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter a prompt for the image.")

# ----------------- Footer ------------------
st.markdown("---")
st.caption("Built with ❤️ by Ahmad Hassan — Open-source tools for everyone.")
