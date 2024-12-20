
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

## **Development Process and Decisions**
### **Understanding the Task**
It was important for us to carefully read and understand the assignment to fully grasp the task at hand. From the first assignment, we had already gained valuable insights into managing similar projects. However, this assignment posed unique challenges that required further reflection, discussion, and exchanges with two other groups to clarify expectations.

### **Planning**
After understanding the requirements, we began brainstorming how we would implement the solution. The professor mentioned Python as a viable language, and due to our extensive experience with Python, we decided to use it. Initially, we debated whether to use .py files or .ipynb files. After discussions, we concluded that .py files would align better with the modularity and structure required to mimic a microkernel architecture.

### **Module Creation**
The assignment provided clear guidelines for the core module, which needed to:

Read text from a file and write processed text back to a file.
Provide a simple mechanism for users to select which plugin to apply to the text.
Load and manage plugins dynamically, ensuring the core remained functional even if no plugins were available.

We started by implementing the core module with these functionalities. To test our work, we developed a small test plugin and added test lines of code. After some minor adjustments, the module worked as intended, allowing us to proceed.

### **Plugins**
We brainstormed ideas for plugins that would be useful and aligned with the assignment's goals. While some ideas were quite creative—like a plugin that rewrites text from back to front—we aimed for a balance between usability and interesting functionality. With some help from brainstorming and suggestions from ChatGPT, we decided on the following six plugins:

1. Keyword Extractor
2. Palindrome Finder
3. Sentiment Analysis
4. Text Summarizer
5. Unique Words
6. Word Counter

These plugins were chosen for their practical utility in text processing and their ability to showcase the tool’s modular capabilities. The sentiment analysis plugin was a late addition, influenced by our experience with similar tasks in other courses.

### **Plugin Implementation**
The implementation of most plugins, such as the Word Counter, was straightforward. However, the Text Summarizer and Sentiment Analysis plugins required integration with the transformers library, which initially caused significant challenges. Installing and configuring the library was particularly tricky, leading us to document the process thoroughly in this README file to help others avoid similar frustrations.

At one point, we considered switching to an API like ChatGPT for these plugins but decided against it to avoid complicating the existing code. Ultimately, after much trial and error, we resolved the issues with transformers and successfully integrated the plugins.

### **Testing**
Extensive testing revealed that the tool worked as intended. However, additional testing with diverse text files uncovered a few issues:

1. We could only apply one plugin at a time.
2. The core had compatibility issues with UTF-8 encoding.
3. The Palindrome Finder didn’t handle uppercase and lowercase letters consistently, nor did it perform well with longer texts.

We addressed these issues by:

- Modifying the core to allow multiple plugin selection and UTF-8 compatibility.
- Enhancing the Palindrome Finder to normalize text for case sensitivity and better handle longer inputs.

### **Conclusion**
This project showcases how a microkernel architecture can be effectively applied to a text processing tool. The modular structure allows for easy extension and customization while ensuring the core remains stable. The process involved planning, problem-solving, and collaboration, resulting in a functional and user-friendly tool.