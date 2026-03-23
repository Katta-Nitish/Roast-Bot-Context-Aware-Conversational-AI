# 🔥 The Roast Bot

A snarky, sarcastic AI-powered chatbot that roasts your statements — built with **Streamlit** and **Google Gemini**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-orange?logo=google)

---

## 🤔 What is this?

You type something. The bot roasts you for it. That's it. No feelings spared.

> **User:** I love coding in Python.  
> **Bot:** Wow, you learned `print('hello world')`, somebody give this genius a medal.

---

## ✨ Features

- 🎭 Witty, sarcastic responses powered by **Gemini 2.5 Flash**
- 🖼️ Custom bot avatar support via `logo.png`
- 🔑 Bring your own Gemini API key via the **sidebar** (optional)
- ⚡ Simple and clean two-column UI built with **Streamlit**
- 🔒 Default API key managed securely via Streamlit Secrets

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| UI Framework | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| Image Processing | Pillow |
| HTTP Requests | requests |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Katta-Nitish/Roast-Bot-Context-Aware-Conversational-AI.git
cd the-roast-bot
```

### 2. Install dependencies

```bash
pip install streamlit pillow requests
```

### 3. Set up your Gemini API key

Create a `.streamlit/secrets.toml` file in the project root:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

> 🔑 Get your free API key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. (Optional) Add a logo

Place a `logo.png` in the project root to display a custom bot avatar. If not found, a 🔥 emoji is shown as fallback.

### 5. Run the app

```bash
streamlit run The_RoastBot.py
```

Then open your browser to `http://localhost:8501`.

---

## 🔑 Using Your Own API Key

Don't want to set up `secrets.toml`? No problem. You can enter your own Gemini API key directly in the **sidebar** at runtime — it takes priority over the default key.

> Get a free key at [Google AI Studio](https://aistudio.google.com/)

---

## 📁 Project Structure

```
the-roast-bot/
├── The_RoastBot.py       # Main app
├── logo.png              # (Optional) Custom bot avatar
├── .streamlit/
│   └── secrets.toml      # API key (do NOT commit this)
└── README.md
```

---

## ⚠️ Important

- **Never commit your `secrets.toml`** — add it to `.gitignore`:
  ```
  .streamlit/secrets.toml
  ```

---
