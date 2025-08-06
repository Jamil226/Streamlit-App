import streamlit as st
import random
import string

# ----------------- Page Config ------------------
st.set_page_config(page_title="Random Generator", page_icon="🎲", layout="centered")

# ----------------- Sidebar ------------------
st.sidebar.title("Tools")
tool = st.sidebar.radio("Choose a Tool", ["Random Name Generator", "Random Password Generator"])

st.sidebar.markdown("---")
st.sidebar.info("Creating open-source tools for the betterment of all.")

# ----------------- Utility Functions ------------------

def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Lee", "Martin", "Walker"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

# ----------------- Main UI ------------------

st.title("Random Generator Hub")

if tool == "Random Name Generator":
    st.subheader("Random Name Generator")
    if st.button("Generate Name"):
        st.success(f"Generated Name: `{generate_random_name()}`")

elif tool == "Random Password Generator":
    st.subheader("Random Password Generator")
    length = st.slider("Password Length", 8, 32, 12)
    if st.button("Generate Password"):
        password = generate_random_password(length)
        st.success(f"Generated Password: `{password}`")
        st.caption("Keep it safe")

# ----------------- Footer ------------------
st.markdown("---")
st.caption("Refresh the app to regenerate or try another tool.")
