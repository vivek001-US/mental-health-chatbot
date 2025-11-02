import streamlit as st
import json
import os
from datetime import datetime
from chatbot_response import get_chatbot_reply
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ✅ Fix for macOS file path (works regardless of OS)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "wellness_tips.json")

# Load wellness tips safely
try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        tips = json.load(f)
except FileNotFoundError:
    st.error("⚠️ Could not find 'wellness_tips.json' in the data folder.")
    tips = {}

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("🧠 AI Mental Health Chatbot")
st.write("Hello! I'm here to listen and support you. Just type how you're feeling below 👇")

user_input = st.text_input("📝 Your Message")

if user_input:
    # Sentiment analysis
    sentiment_score = analyzer.polarity_scores(user_input)["compound"]
    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    st.write(f"**Detected Emotion:** {sentiment}")

    # Get chatbot reply
    reply = get_chatbot_reply(user_input)
    st.markdown(f"**🤖 Chatbot:** {reply}")

    # Display a wellness tip
    if isinstance(tips, dict):
        tip = tips.get(sentiment.lower(), "Take a deep breath. You got this 💚")
        st.info(f"🌿 Wellness Tip:\n\n{tip}")
    elif isinstance(tips, list) and tips:
        st.info(f"🌿 Wellness Tip:\n\n{tips[0]}")
    else:
        st.info("🌿 Take care of yourself — small steps matter.")

    # Log conversation (mac-safe file path)
    log_file = os.path.join(BASE_DIR, "chat_logs.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}\nUser: {user_input}\nBot: {reply}\n\n")
