# sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# Initialize once (more efficient on Mac M2)
analyzer = SentimentIntensityAnalyzer()

def clean_text(text: str) -> str:
    """Preprocess and clean user text for better sentiment analysis."""
    text = text.strip().lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars/numbers
    return text

def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment of input text using VADER.
    Returns both the label (Positive/Negative/Neutral) and numeric score.
    """

    if not text or not text.strip():
        return {"sentiment": "Neutral", "score": 0.0}

    # Clean text for better accuracy
    cleaned_text = clean_text(text)

    # Get VADER sentiment scores
    score = analyzer.polarity_scores(cleaned_text)
    compound = score['compound']

    # Adjusted thresholds for more emotional sensitivity
    if compound >= 0.25:
        sentiment = "Positive"
    elif compound <= -0.25:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"sentiment": sentiment, "score": round(compound, 3)}
