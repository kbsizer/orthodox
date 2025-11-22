#!/usr/bin/env python
"""
Setup Instructions

1) Install the SDK: Open your terminal and run the following command:

        $ pip install google-genai

2) Get Your API Key: Create a Gemini API key from Google AI Studio.

3) Set Environment Variable: Set the API key as an environment variable named GEMINI_API_KEY.

        Linux/macOS: export GEMINI_API_KEY="YOUR_API_KEY"

        Windows (CMD): set GEMINI_API_KEY="YOUR_API_KEY"

        Windows (PowerShell): $env:GEMINI_API_KEY="YOUR_API_KEY"

4) Run the Script: Save the code above as a Python file (e.g., run_gemini.py) and execute it:

        $ python run_gemini.py
"""

import os
from google import genai

# --- Configuration ---
# Set your API Key as an environment variable (GEMINI_API_KEY)
# The client will automatically pick it up.
# You can get a key from Google AI Studio.
API_KEY_ENV_VAR = "GEMINI_API_KEY"
MODEL_NAME = "gemini-2.5-flash"
OUTPUT_FILE = "gemini_responses.txt"
PROMPT = "Write a short, engaging summary about the importance of using clean, reusable code components."


def get_gemini_response(prompt: str) -> str:
    """
    Calls the Gemini API with the given prompt and returns the text response.

    Args:
        prompt: The text prompt to send to the model.

    Returns:
        The generated text response from the model.
    """
    try:
        # The client automatically uses the GEMINI_API_KEY environment variable.
        client = genai.Client()

        print(f"Submitting prompt to model: {MODEL_NAME}...")

        # Call the generate_content method
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

        return response.text

    except Exception as e:
        print(f"An error occurred during API call: {e}")
        print("Please ensure your API key is set correctly in your environment.")
        return f"[API ERROR: {e}]"


def append_to_file(filename: str, prompt: str, response_text: str):
    """
    Appends the prompt and the model response to the specified text file.

    Args:
        filename: The path to the file to append to.
        prompt: The user-submitted prompt.
        response_text: The generated response from the model.
    """
    try:
        # Use 'a' for append mode. This creates the file if it doesn't exist.
        with open(filename, "a", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write(f"PROMPT: {prompt}\n")
            f.write("-" * 50 + "\n")
            f.write(f"RESPONSE:\n{response_text}\n")
            f.write("=" * 50 + "\n\n")

        print(f"Successfully appended response to **{filename}**.")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")


def main():
    if not os.getenv(API_KEY_ENV_VAR):
        print(f"FATAL: {API_KEY_ENV_VAR} environment variable not found.")
        print("Please set your Gemini API key as an environment variable.")
        return

    # 1. Get response from Gemini
    response_text = get_gemini_response(PROMPT)

    if "[API ERROR" not in response_text:
        # 2. Append to file
        append_to_file(OUTPUT_FILE, PROMPT, response_text)


if __name__ == "__main__":
    main()
