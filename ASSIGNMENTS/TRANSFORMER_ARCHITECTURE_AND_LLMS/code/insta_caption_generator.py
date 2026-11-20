"""Session 5 - Streamlit LLM app (Tasks 1-5).
Run with:   pip install streamlit requests
            set OPENAI_API_KEY=sk-...        (Windows)   |   export OPENAI_API_KEY=sk-...   (Mac/Linux)
            streamlit run insta_caption_generator.py
If no API key is found the app still works, using a small offline caption generator, so it never crashes."""
import os
import random
import requests
import streamlit as st

# ---- Task 1: main-page text ----
st.title("Welcome to Insta Caption Generator!")

API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"


def generate_caption(description: str) -> str:
    """Task 4: call the OpenAI GPT API with `requests` and return an Instagram caption."""
    api_key = os.getenv("OPENAI_API_KEY") or st.session_state.get("api_key", "")
    if not api_key:                                       # offline fallback so the demo always works
        tags = " ".join("#" + w.strip(".,!").lower() for w in description.split()[:3] if len(w) > 3)
        return random.choice(["Living for moments like this ✨", "Caught in the good light 🌅", "Some days just feel like a postcard 📸"]) + " " + tags
    payload = {"model": MODEL, "max_tokens": 60, "temperature": 0.9,
               "messages": [{"role": "system", "content": "You write short, catchy Instagram captions with 2-3 hashtags and one emoji."},
                            {"role": "user", "content": "Write a caption for this photo: " + description}]}
    try:
        r = requests.post(API_URL, headers={"Authorization": "Bearer " + api_key}, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:                                # network / key / quota problems
        return "Sorry, could not fetch a caption (%s)." % e


if "history" not in st.session_state:
    st.session_state.history = []                         # list of (description, caption)

with st.sidebar:
    st.text_input("OpenAI API key (optional)", type="password", key="api_key")

# ---- Task 2: UI ----
description = st.text_input("Describe your photo")
clicked = st.button("Generate Caption")

# ---- Task 3 + 4 + 5: show the input, fetch the caption, keep chat history ----
if clicked and description.strip():
    st.write("**Your Description:**", description)
    caption = generate_caption(description)
    st.session_state.history.append((description, caption))
    st.success(caption)

# ---- Task 5: chat interface showing the last 3 exchanges as chat bubbles ----
if st.session_state.history:
    st.subheader("Recent captions")
    for user_text, ai_text in st.session_state.history[-3:]:
        with st.chat_message("user"):
            st.write(user_text)
        with st.chat_message("assistant"):
            st.write(ai_text)
