import streamlit as st
import random
import string
import json

# ----------------- Page Config ------------------
st.set_page_config(page_title="Random Generator", page_icon="🎲", layout="centered")

# ----------------- Sidebar ------------------
st.sidebar.title("🧰 Tools")
tool = st.sidebar.radio("Choose a Tool", ["Random Name Generator", "Random Password Generator"])

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
    else:  # All (Letters + Numbers + Special Characters)
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

# ----------------- Main UI ------------------

st.title("🎲 Random Generator Hub")

if tool == "Random Name Generator":
    st.subheader("📛 Random Name Generator")
    if st.button("Generate Name"):
        st.success(f"Generated Name: `{generate_random_name()}`")

elif tool == "Random Password Generator":
    st.subheader("🔑 Random Password Generator")
    
    # Password length and mode selection
    length = st.slider("Password Length", 8, 32, 12)
    mode = st.selectbox("Password Type", ["Letters Only", "Numbers Only", "Letters + Numbers", "All"])

    if st.button("Generate Password"):
        password = generate_random_password(length, mode)
        st.success(f"Generated Password: `{password}`")
        st.caption("Keep it secure 🔐")

# ----------------- Footer ------------------
st.markdown("---")
st.caption("Built with ❤️ by Muhammad Jamil — Open-source tools for everyone.")
