# Chat with File AI Chatbot

## Overview

This Python script allows you to interact with a Google Generative AI chatbot that has been trained on the content of a chosen file. It leverages Google's context caching feature to provide efficient and cost-effective interactions by "remembering" the file content for a specified time.

## Key Features

- **Model Selection:** Choose between two AI models for specific needs: "gemini-1.5-flash-001" or "gemini-1.5-pro-001".
- **File Listing:** Lists all files in the current directory for easy selection.
- **Time-Tracked File Processing:** Monitors and displays the elapsed time during file upload and processing.
- **Context Caching:** Efficiently manages the AI's memory of the file content to provide fast and relevant responses.
- **Interactive Chat:** Engage in a conversational manner with the AI based on the uploaded file's content.
- **Exit Command:** Easily terminate the session by typing "exit" or "quit".

## Why This is Cool

- **Cost-Effective:** You're charged less because the AI doesn't need to re-process the entire file for each question.
- **Speed:** Responses are faster because the AI already knows the context.
- **Great for Big Stuff:** Perfect for large files or if you have many questions about the same content.

## Important Notes

- **API Key:** You need a Google Generative AI API key to use this. Replace "YOUR_API_KEY" in the code.
- **File Size:** There are limits to how big the file can be.
- **Cost:** While more cost-effective, using the AI still has costs associated with it.

## Before Running

1. **Install Python:** Make sure you have Python installed on your computer. You can download it from [Python Downloads](https://www.python.org/downloads/).
2. **Install Libraries:** Open your terminal or command prompt and run the following command to install the necessary libraries:
   ```sh
   pip install google-generativeai
   ```

## How to Run

1. **Replace API Key:** Replace "YOUR_API_KEY" in the script with your actual Google Generative AI API key.
2. **Save the Script:**
   Save the script as a `.py` file (e.g., `chat_with_file.py`).
3. **Directory Setup:**
   Place the file you want to upload in the same directory as the script.
4. **Run the Script:**
   Open your terminal or command prompt and navigate to the script's directory.
   Run the script using:
   ```sh
   python chat_with_file.py
   ```

## Usage

1. **Select AI Model:**
   At the start, select the AI model you want to use from the provided list.
2. **Select File:**
   The script will list the files in the current directory. Enter the number corresponding to the file you want to use.
3. **Chat:**
   Start chatting with the AI! Type your questions or messages, and the AI will respond based on the file's content.
4. **Exit:**
   Type "exit" or "quit" to end the conversation.

## Contributing

Feel free to submit issues and enhancement requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Google Generative AI](https://cloud.google.com/ai-platform/generative-ai) and its documentation for enabling the functionalities used in this script.

By following the steps outlined in this README, you should be able to easily set up and interact with the file-based AI chatbot. Enjoy chatting!
