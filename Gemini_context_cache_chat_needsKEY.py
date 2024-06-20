# --- Overview ---
# This script allows you to chat with an AI chatbot that has been trained on the content of a file you choose.
# It leverages Google Gemini API's *context caching* feature for efficient and cost-effective interactions.
# It only accepts up to 10 minutes and 41 seconds of video. 
# It has a minimum input token count of 32,768 (only super large docs or media files)

# --- What is Context Caching? ---
# Imagine telling the AI about a long movie. Instead of reminding it about every detail each time you ask a question,
# context caching lets you "upload" the movie information once. The AI then remembers it for a set time,
# making conversations faster and cheaper, especially if you ask many questions about the same content.

# --- How This Script Uses It ---
# 1. **Model Selection:** You first select from available AI models ("gemini-1.5-flash-001" or "gemini-1.5-pro-001").
# 2. **File Upload:** You choose a file (like a movie script or a long document). The script uploads it to Google's AI system.
# 3. **Creating a "Memory":** The uploaded file is turned into a special "memory" for the AI. Think of this as the AI reading and remembering the file.
# 4. **Chatting:** You can now ask questions related to the file. The AI uses its "memory" to answer without needing the file repeatedly.
# 5. **Time Limit:** The AI's memory lasts for a set time (defined in the script). After that, it forgets to save costs.

# --- Key Features ---
# - **Model Selection:** Choose from two AI models for your specific needs.
# - **File Listing:** Lists all files in the current directory for easy selection.
# - **Time-Tracked File Processing:** Monitors and displays the elapsed time during file upload and processing.
# - **Context Caching:** Efficiently manages the AI's memory of the file content to provide fast and relevant responses.
# - **Interactive Chat:** Engage in a conversational manner with the AI based on the uploaded file's content.
# - **Exit Command:** Easily terminate the session by typing "exit" or "quit".

# --- Why This is Cool ---
# - **Cost-Effective:** You're charged less because the AI doesn't have to re-process the entire file for each question.
# - **Speed:** Responses are faster because the AI already knows the context.
# - **Great for Big Stuff:** Perfect for large files or if you have many questions about the same content.

# --- Important Notes ---
# - **API Key:** You need a Google Generative AI API key to use this. Replace "YOUR_API_KEY" in the code.
# - **File Size:** There are limits to how big the file can be.
# - **Cost:** While cheaper, using the AI still has costs associated with it.

# --- Before Running ---
# 1. Install Python: Make sure you have Python installed on your computer. You can download it from https://www.python.org/downloads/.
# 2. Install Libraries: Open your terminal or command prompt and run the following command to install the necessary libraries:
#    pip install google-generativeai

# --- How to Run ---
# 1. Replace "YOUR_API_KEY" below with your actual Google Generative AI API key.
# 2. Save this script as a .py file (e.g., chat_with_file.py).
# 3. Place the file you want to use in the same directory as the script.
# 4. Open your terminal or command prompt and navigate to the directory containing the script.
# 5. Run the script using the command: python chat_with_file.py
# 6. Select the AI model you want to use from the provided list.
# 7. The script will list the files in the directory. Enter the number corresponding to the file you want to use.
# 8. Start chatting with the AI! Type your questions or messages, and the AI will respond based on the file's content.
# 9. Type "exit" or "quit" to end the conversation.

import os  # Module for interacting with the operating system
import sys  # Module for interacting with the system-specific parameters and functions
import time  # Module for handling time-related tasks
import datetime  # Module for handling date and time
import google.generativeai as genai  # Module for Google Generative AI functionalities

# --- Virtual Environment Setup --- 
# It's a good practice to use virtual environments because they create isolated environments for your Python projects, 
# helping to manage dependencies and avoid conflicts.
venv_path = '.venv'

# Function to activate the virtual environment
def activate_venv():
    # Path to the activation script of the virtual environment
    activate_script = os.path.join(venv_path, 'bin', 'activate_this.py')
    if os.path.exists(activate_script):
        # If the activation script exists, read and execute it
        with open(activate_script, 'r') as f:
            exec(f.read(), {'__file__': activate_script})
    else:
        # Print a warning if the virtual environment doesn't exist
        print(f"Warning: Virtual environment not found at '{venv_path}'.", file=sys.stderr)

# Call to activate the virtual environment
activate_venv()

# --- Configuration ---
# Configure the API key for Google Generative AI (Replace "YOUR_API_KEY" with your actual key)
genai.configure(api_key="YOUR_API_KEY")
# Set the time to keep data cached in minutes
CACHE_TTL_MINUTES = 15  
# Default AI model name to be used
MODEL_NAME = "models/gemini-1.5-pro-001"  
# ANSI escape codes for colored text (Green for the AI response)
GREEN = "\033[92m"  
RESET = "\033[0m"  

# --- Functions ---

# Function to list all files in the current working directory
def list_files_in_cwd():
    # Get a list of files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # Print the list of files with a numbered index
    print("Files in current directory:")
    for index, file in enumerate(files):
        print(f"{index + 1}. {file}")
    return files

# Function to get the user's choice of file from the listed files
def get_user_file_choice(files):
    while True:
        try:
            # Ask the user to enter the number of the file to use
            choice = int(input(f"Enter the number of the file to use: "))
            if 1 <= choice <= len(files):
                # If the user's choice is valid, return the chosen file
                return files[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to upload and process the selected file, tracking the time elapsed
def upload_and_process_file(file_path):
    # Start time for the upload process
    start_time = time.time()
    
    # Upload the file to Google Generative AI
    uploaded_file = genai.upload_file(path=file_path)
    file_size = os.path.getsize(file_path)

    # File upload progress indicator
    while True:
        uploaded_file = genai.get_file(uploaded_file.name)
        
        # Calculate elapsed time in seconds
        elapsed_time = time.time() - start_time
        # Convert elapsed time to a readable format (minutes and seconds)
        minutes, seconds = divmod(elapsed_time, 60)
        
        print(f"Current state: {uploaded_file.state.name} (Elapsed Time: {int(minutes)}m {int(seconds)}s)")
        
        if uploaded_file.state.name == "ACTIVE":
            # If the file is ready (ACTIVE), break the loop
            break
        elif uploaded_file.state.name in ["FAILED", "CANCELLED"]:
            # If the file upload failed or was cancelled, raise an exception
            raise Exception(f"File processing failed with state: {uploaded_file.state.name}")

        print(f"Waiting for {file_path} to process... (Elapsed Time: {int(minutes)}m {int(seconds)}s)")
        # Wait for 2 seconds before checking the status again
        time.sleep(2)

    print(f"File processed in {int(minutes)}m {int(seconds)}s: {uploaded_file.uri}")
    # Return the details of the uploaded file
    return uploaded_file

# Function to create a cached model from the uploaded file for efficient processing
def create_cached_model(uploaded_file):
    # Define the instructions given to the AI model
    system_instruction = (
        "You are an AI assistant trained on the provided file. "
        "Answer user questions based on its content."
    )
    # Create a cached content object with the uploaded file and system instructions
    cache = genai.caching.CachedContent.create(
        model=MODEL_NAME,
        display_name=os.path.basename(uploaded_file.name),
        system_instruction=system_instruction,
        contents=[uploaded_file],
        ttl=datetime.timedelta(minutes=CACHE_TTL_MINUTES),
    )
    # Create and return a GenerativeModel using the cached content
    return genai.GenerativeModel.from_cached_content(cached_content=cache)

# --- Main Program ---
def main():
    # Allow the user to select the model
    models = ["gemini-1.5-flash-001", "gemini-1.5-pro-001"]
    print("Available AI models:")
    for idx, model in enumerate(models, start=1):
        print(f"{idx}. {model}")
    
    while True:
        try:
            model_choice = int(input("Select the AI model by entering the corresponding number: "))
            if 1 <= model_choice <= len(models):
                selected_model = models[model_choice - 1]
                print(f"Selected model: {selected_model}")
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Use the selected model for subsequent operations
    global MODEL_NAME
    MODEL_NAME = f"models/{selected_model}"

    # List the files in the current directory and allow the user to choose one
    files = list_files_in_cwd()
    chosen_file = get_user_file_choice(files)

    # Upload and process the chosen file
    uploaded_file = upload_and_process_file(chosen_file)
    # Create a cached model from the uploaded file
    model = create_cached_model(uploaded_file)

    print(f"Using content from: {chosen_file}")
    print("Welcome! Chat with the model based on the file's content.")

    # Loop to chat with the AI model
    while True:
        user_input = input("> ")  # Get user input (their question or message)
        if user_input.lower() in ["exit", "quit"]:  # If the user wants to quit
            print("Exit command recognized. Preparing to exit.")
            print("Goodbye!")
            break

        # Generate AI response based on user input
        response = model.generate_content([user_input], stream=True)
        try:
            # Print usage metadata for debugging purposes (not typically needed for end-users)
            print(response.usage_metadata)

            # Print the AI's response in green
            for chunk in response:
                if hasattr(chunk, 'text'):
                    print(f"{GREEN}{chunk.text}{RESET}")
                else:
                    print("No text found in this chunk.")
        except Exception as e:
            print(f"An error occurred while processing the response: {e}")

# If this script is executed, run the main function
if __name__ == "__main__":
    main()