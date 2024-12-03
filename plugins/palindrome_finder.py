import re

def process(text: str) -> str:
    """
    Finds and lists all palindromes in the text.
    :text: Input text to analyze.
    :return: List of palindromes.
    """
    try:
        # Normalize the text: remove punctuation and convert to lowercase
        words = re.findall(r'\b\w+\b', text.lower())  # Extract words only
        palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
        
        if palindromes:
            return f"Palindromes: {', '.join(sorted(set(palindromes)))}"
        else:
            return "No palindromes found."
    except Exception as e:
        return f"Error finding palindromes: {e}"
