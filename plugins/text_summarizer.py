from transformers import pipeline

# Load the summarization model
summarizer = pipeline('summarization')

def process(text: str) -> str:
    """
    Summarizes the input text.
    :param text: Input text to summarize.
    :return: Summarized text.
    """
    try:
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        return f"Summary: {summary[0]['summary_text']}"
    except Exception as e:
        return f"Error summarizing text: {e}"
