# 🎲 Random Generator Hub

Welcome to **Random Generator Toolkit** — a simple and powerful open-source Streamlit app that lets you generate:

- Random full names (from a dataset of 1000+ names)
- Strong, customizable random passwords

Empowering people through open-source innovation.

---

## Live Demo

🟢 Try it here: [jamil226.streamlit.app/](https://jamil226.streamlit.app/)

---

## Features

### 🔐 Random Password Generator

- Choose password length (8–32 characters)
- Choose character types:
  - Letters Only (A–Z, a–z)
  - Numbers Only (0–9)
  - Letters + Numbers
  - Letters + Numbers + Special Characters

### 📛 Random Name Generator

- Generates random full names from a JSON dataset of 1000+ entries
- Great for demos, testing, placeholder data

---

## Tech Stack

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- JSON for name dataset
- Hosted on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Project Structure

random-generator-app/
├── app.py
├── requirements.txt
├── random_names_1000.json
└── .streamlit/
└── config.toml (optional for theming)

---

## ▶️ How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/Jamil226/Streamlit-App

```

## Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

## Install dependencies

```bash
pip install -r requirements.txt # On Windows: venv\Scripts\activate

```

## Run the app

```bash
streamlit run app.py # On Windows: venv\Scripts\activate

```
