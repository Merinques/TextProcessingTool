def process(text: str) -> str:
    """
    Identifies and lists all unique words in the text.
    :text: Input text to analyze.
    :return: Count and list of unique words.
    """
    try:
        words = set(text.split())
        return f"Unique words ({len(words)}): {', '.join(sorted(words))}"
    except Exception as e:
        return f"Error identifying unique words: {e}"
