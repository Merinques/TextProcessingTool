from transformers import pipeline

# Load the sentiment analysis model
sentiment_analyzer = pipeline('sentiment-analysis')

def process(text: str) -> str:
    """
    Analyzes the sentiment of the text.
    :param text: Input text to analyze.
    :return: Sentiment result with label and score.
    """
    try:
        result = sentiment_analyzer(text[:512])  # Limiting input size for the API
        sentiment = result[0]['label']
        score = result[0]['score']
        return f"Sentiment: {sentiment}, Confidence Score: {score:.2f}"
    except Exception as e:
        return f"Error analyzing sentiment: {e}"
