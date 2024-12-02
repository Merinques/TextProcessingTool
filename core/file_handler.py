def load_file(file_path: str) -> str:
    """
    Load text from a file with UTF-8 encoding.
    :param file_path: Path to the input text file.
    :return: Text content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return ""
    except UnicodeDecodeError as e:
        print(f"Error reading file: Encoding issue - {e}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def save_file(file_path: str, content: str) -> None:
    """
    Save text to a file with UTF-8 encoding.
    :param file_path: Path to save the processed text file.
    :param content: Text content to save.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding
            file.write(content)
        print(f"File saved successfully to {file_path}.")
    except Exception as e:
        print(f"Error saving file: {e}")
