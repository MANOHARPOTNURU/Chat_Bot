# Simple Gemini Chatbot

A basic command-line chat application powered by Google's Gemini AI model, allowing users to have interactive conversations with an AI bot.

## Key Features

* Connects to the Gemini AI model.
* Allows users to input text and receive responses.
* Basic "bye" command to exit the chat.
* Customizable bot name.

## Getting Started

### Prerequisites

* Python 3 installed on your system.
* A Google Cloud account with access to the Gemini API and an API key. **Important: Do not hardcode your API key directly in the script.** Refer to the [Google Cloud AI Platform documentation]) for instructions on obtaining an API key.
* The `google-generativeai` Python library installed.

### Installation

1.  Clone the repository:
    ```bash
    git clone [your-repository-url]
    cd simple-gemini-chatbot
    ```
2.  Install the required library:
    ```bash
    pip install google-generativeai
    ```
3.  **Setting up the API Key (Recommended: Environment Variable):**
   ***** get your API key for ftree from : Google AI Studio   *****
    Set your Gemini API key as an environment variable named `API_KEY`:
    ```bash
    export API_KEY="YOUR_ACTUAL_API_KEY"
    ```
    (Replace `"YOUR_ACTUAL_API_KEY"` with your actual API key).

5.  Running the script:
    ```bash
    python your_chat_script.py
    ```
    (Replace `your_chat_script.py` with the name of your Python file).

## Usage

Once the script is running, you will be prompted to enter your name and the name for the bot. After that, you can start typing your messages. Type `bye` to exit the chat.
