from collections import Counter
import re

def process(text: str) -> str:
    """
    Extracts and lists the most common keywords in the text.
    :param text: Input text to analyze.
    :return: List of top keywords and their frequencies.
    """
    try:
        # Normalize and split text into words
        words = re.findall(r'\b\w+\b', text.lower())  # Extract words only
        word_counts = Counter(words)
        # Get the top 10 most common words
        top_keywords = word_counts.most_common(10)
        return f"Top Keywords: {top_keywords}"
    except Exception as e:
        return f"Error extracting keywords: {e}"
