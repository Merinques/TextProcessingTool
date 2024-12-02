
# **Text Processing Tool**

## **Overview**
This Text Processing Tool uses a microkernel architecture to process text files with modular plugins. Each plugin performs a specific task, such as sentiment analysis, keyword extraction, or summarization. The tool is designed to be extensible and easy to use.

---

## **Setup Instructions**

### 1. **Download the Tool**
- Clone or download the project repository from your source (e.g., GitHub, shared drive).

### 2. **Install Required Libraries**
- Open a terminal in the project folder and install the necessary Python libraries:
  ```bash
  pip install transformers torch tensorflow nltk regex
  ```
- Ensure both **PyTorch** and **TensorFlow** are installed, as they are required for various plugins:
  - Install **PyTorch** (CPU-only version):
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ```
  - Alternatively, visit [PyTorch Installation Guide](https://pytorch.org/get-started/locally/) for GPU support.
  - Install **TensorFlow**:
    ```bash
    pip install tensorflow
    ```

### 3. **Enable Long Path Support (Windows Only)**
- Windows may encounter issues with long file paths. To enable long path support:
  - Run the following PowerShell command with administrator privileges:
    ```powershell
    New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
    -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
    ```
  - Restart your computer.
- For more details, refer to the [official documentation](https://pip.pypa.io/warnings/enable-long-paths).

### 4. **Navigate to the Project Directory**
- Open a terminal or command prompt.
- Change to the project folder where the tool is located:
  ```bash
  cd path/to/Assignment2
  ```

### 5. **Run the Main Script**
- Start the tool by running:
  ```bash
  python main.py
  ```

---

## **Using the Tool**

### 1. **Provide a Text File Path**
- When prompted, enter the full path to the text file you want to process. For example:
  ```
  C:\Users\YourUsername\Documents\sample_text.txt
  ```

### 2. **Choose Plugins**
- A list of available plugins will be displayed. Select one or more plugins by entering their numbers separated by commas (e.g., `1,3,5`).

### 3. **Save the Processed Data**
- After the selected plugins have processed the text, you will be prompted to save the output. Enter the full path to the output file, including the filename. For example:
  ```
  C:\Users\YourUsername\Documents\processed_text.txt
  ```

### 4. **Done!**
- The processed data is saved, and you can view it in the output file.

---

## **Available Plugins**

- **Keyword Extractor**: Extracts and lists the most common keywords in the text.
- **Palindrome Finder**: Identifies palindromes in the text.
- **Sentiment Analysis**: Analyzes the sentiment of the text (e.g., positive, negative, neutral).
- **Text Summarizer**: Condenses the text into a shorter version while preserving its meaning.
- **Unique Words**: Lists all unique words and their count.
- **Word Counter**: Counts the total number of words in the text.

---

## **How It Works**
1. The **core** of the tool handles loading text files, saving processed data, and managing plugins.
2. Each plugin processes the text independently, offering modular and extensible functionality.
3. The tool leverages the Hugging Face `transformers` library for advanced features like sentiment analysis and summarization, powered by **PyTorch** and **TensorFlow**.

---

## **Troubleshooting**

- **Encoding Issues**:
  - If you encounter errors related to file encoding, ensure the input text file is saved in **UTF-8 format**.
  - Open the file in a text editor and save it as UTF-8 if needed.

- **Library Not Found**:
  - If you see errors about missing libraries, ensure you’ve installed all dependencies:
    ```bash
    pip install transformers torch tensorflow nltk regex
    ```

- **Path Issues**:
  - Use double backslashes (`\\`) or forward slashes (`/`) in file paths on Windows.
  - Example:
    ```
    C:\\Users\\YourUsername\\Documents\\sample_text.txt
    ```

---

## **Example Workflow**

### 1. **Run the Tool**:
```bash
python main.py
```

### 2. **Input File Path**:
```
Enter the path to the text file: C:\Users\YourUsername\Documents\sample_text.txt
```

### 3. **Select Plugins**:
```
Select one or more plugins to apply by entering their numbers separated by commas (e.g., 1,3,5): 1,3,5
```

### 4. **Save the Processed File**:
```
Enter the path to save the plugin results: C:\Users\YourUsername\Documents\processed_text.txt
```

### 5. **Done!**
- The processed results are saved, and you can view them in `processed_text.txt`.

---

## **Voila!**
You now have a functional and modular text processing tool ready to analyze and process text files efficiently.
