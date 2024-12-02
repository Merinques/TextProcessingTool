import re

def process(text: str) -> str:
    """
    Counts the number of words in the text.
    :param text: Input string
    :return: Word count as a string
    """
    words = re.findall(r'\b\w+\b', text)  # Match words only
    word_count = len(words)
    return f"Word count: {word_count}"
