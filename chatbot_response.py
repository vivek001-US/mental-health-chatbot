# chatbot_response.py
import random
import time

def get_chatbot_reply(user_input):
    """Generate a supportive chatbot reply based on user emotions."""

    text = user_input.lower().strip()

    # Simulate natural typing delay for a human-like response
    time.sleep(0.5)

    # Define response categories
    responses = {
        "sad": [
            "I'm really sorry you're feeling this way. You're not alone. 💙",
            "It’s okay to feel sad sometimes. Remember, healing takes time. 💫",
            "You matter, and your feelings are valid. Take a deep breath. 🌿"
        ],
        "happy": [
            "That’s wonderful! Keep shining bright. 🌟",
            "I’m so glad to hear that! Happiness looks good on you. 😊",
            "Yay! Keep that positive energy flowing! 💛"
        ],
        "anxious": [
            "Anxiety can be tough. Try grounding yourself with deep breaths. 🌬️",
            "It’s okay to pause. Focus on your breathing, one step at a time. 🕊️",
            "You're doing great. Remember, it’s okay to take breaks. 💚"
        ],
        "angry": [
            "It’s okay to feel angry. Try to express it in a healthy way. ❤️‍🔥",
            "Anger is a natural emotion. Let’s take a moment to cool down together. 🧊",
            "I understand. Maybe some music or a short walk could help. 🎧"
        ],
        "tired": [
            "You seem exhausted. Rest is important — you deserve it. 😴",
            "Take a short break or a nap if you can. Your body needs care too. 💤",
            "Try to relax your shoulders and close your eyes for a minute. 🌙"
        ],
        "default": [
            "Thank you for sharing. I'm here for you. 🤗",
            "I'm listening — tell me more about what’s on your mind. 💬",
            "You’re doing your best, and that’s enough. 🌻"
        ]
    }

    # Keyword-based emotional detection
    if any(word in text for word in ["sad", "depressed", "unhappy", "down"]):
        category = "sad"
    elif any(word in text for word in ["happy", "joy", "excited", "great"]):
        category = "happy"
    elif any(word in text for word in ["anxious", "nervous", "worried", "stressed"]):
        category = "anxious"
    elif any(word in text for word in ["angry", "mad", "furious", "irritated"]):
        category = "angry"
    elif any(word in text for word in ["tired", "sleepy", "exhausted", "drained"]):
        category = "tired"
    else:
        category = "default"

    # Pick a random response from the detected emotion
    reply = random.choice(responses[category])
    return reply
