import streamlit as st
import random
import string
import json
import requests
from huggingface_hub import InferenceClient

# ----------------- Page Config ------------------
st.set_page_config(page_title="AI Creativity Toolkit", page_icon="✨", layout="wide")

# ----------------- Sidebar ------------------
st.sidebar.title("🧰 AI Creativity Toolkit")
tool = st.sidebar.radio(
    "Choose a Tool", 
    ["🎨 Text to UI", "🖼️ Text to Image", "🤖 Chatbot"]
)

st.sidebar.markdown("---")
st.sidebar.success("🚀 Create, Design & Imagine with AI — all in one place.")

# ----------------- Hugging Face Token ------------------
HF_TOKEN = st.secrets["HF_TOKEN"]

# ----------------- Hugging Face Clients ------------------
# Text-to-Image client
image_client = InferenceClient(
    provider="auto",   # Let Hugging Face choose the right provider
    api_key=HF_TOKEN,
)

# Chatbot (LLaMA 3.1)
def query_llama3(question: str):
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# ----------------- Optional Random Name / Password Utilities ------------------
@st.cache_data
def load_names():
    with open("random_names.json", "r") as f:
        return json.load(f)

names = load_names()

def generate_random_name():
    person = random.choice(names)
    return f"{person['first_name']} {person['last_name']}"

def generate_random_password(length=12, mode="All"):
    import string
    if mode == "Letters Only":
        chars = string.ascii_letters
    elif mode == "Numbers Only":
        chars = string.digits
    elif mode == "Letters + Numbers":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

# ----------------- Text-to-UI Function ------------------
def text_to_ui(prompt):
    """Generate Python Streamlit UI code using LLaMA 3.1"""
    return query_llama3(f"Write a Streamlit component for this description:\n{prompt}")

# ----------------- Text-to-Image Function ------------------
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
st.title("✨ AI Creativity Toolkit")

if tool == "🎨 Text to UI":
    st.subheader("Generate UI Design from Text")
    ui_prompt = st.text_area(
        "Describe the UI you want (e.g., 'A login form with email, password and a submit button'):"
    )
    if st.button("Generate UI Code"):
        if ui_prompt.strip():
            with st.spinner("Generating UI..."):
                code = text_to_ui(ui_prompt)
                st.code(code, language="python")
        else:
            st.warning("Please enter a UI description.")

elif tool == "🖼️ Text to Image":
    st.subheader("Generate Image from Text")
    img_prompt = st.text_area("Enter your image description (e.g., 'Astronaut riding a horse'):")
    if st.button("Generate Image"):
        if img_prompt.strip():
            with st.spinner("Generating image..."):
                image = text_to_image(img_prompt)
                if image:
                    st.image(image, caption="Generated Image", use_container_width=True)
        else:
            st.warning("Please enter a prompt for the image.")

elif tool == "🤖 Chatbot":
    st.subheader("Chat with LLaMA 3.1")
    user_input = st.text_input("Ask me anything...")
    if user_input:
        with st.spinner("Thinking..."):
            response = query_llama3(user_input)
            st.success(response)

# ----------------- Footer ------------------
st.markdown("---")
st.caption("✨ Built with ❤️ using Streamlit + Hugging Face Inference API")
