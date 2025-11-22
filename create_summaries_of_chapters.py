#!/usr/bin/env python

import argparse
import os
import sys
import time
import glob
from google import genai
from google.genai.errors import APIError as GeminiException

# --- Configuration ---
MODEL_NAME = "gemini-2.5-flash"
# Ensure your GEMINI_API_KEY environment variable is set.


def get_gemini_summary(prompt: str) -> str:
    """
    Calls the Gemini API with the given prompt and returns the text response.
    Handles API exceptions.
    """
    try:
        # The client automatically uses the GEMINI_API_KEY environment variable.
        client = genai.Client()

        # Call the generate_content method
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

        # Check for safety/content issues
        if response.text:
            return response.text
        else:
            # Check the finish reason if text is empty
            reason = (
                response.candidates[0].finish_reason.name
                if response.candidates
                else "UNKNOWN"
            )
            return f"\n[GEMINI ERROR: Content generation failed. Reason: {reason}]"

    except GeminiException as e:
        return f"\n[API ERROR: Gemini API request failed: {e}]"
    except Exception as e:
        return f"\n[GENERAL ERROR: An unexpected error occurred: {e}]"


def process_chapters(start_index: int, end_index: int):
    """
    Iterates through chapter numbers, reads the file, builds the prompt,
    and prints the Gemini summary to STDOUT.
    """
    print(
        f"--- Starting Chapter Summary from {start_index:02d} to {end_index:02d} ---",
        file=sys.stderr,
    )

    # Iterate through the chapter numbers inclusive of end_index
    for chapter_num in range(start_index, end_index + 1):

        # Format the chapter number with leading zeros (e.g., 1 -> 01)
        nn = f"{chapter_num:02d}"

        # Use glob to find the file pattern Chapter-nn-*.txt
        # This handles cases where the full file name suffix might vary
        search_pattern = f"Chapter-{nn}-*.txt"
        file_matches = glob.glob(search_pattern)

        if not file_matches:
            # Print status messages to STDERR so they don't pollute the summary output (STDOUT)
            print(
                f"File not found for Chapter {nn}. Skipping. (Searched for: {search_pattern})",
                file=sys.stderr,
            )
            continue

        # We assume the first match is the correct file
        file_path = file_matches[0]

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}", file=sys.stderr)
            continue

        # --- 4. Build the Gemini Prompt ---
        prompt = f"""\
Please provide a concise summary of the following text. The summary should consist of three sections: \
A 2-3 line high-level summary of the text, a bullet list of characters with a short (1 line) description of each, \
and a bullet list of the 3 to 7 main events which take place in the text. Bullet list items should be no more than 2 lines. \
They should focus on what happened and what is said, not interpretations of it.\
The output for each chapter should be formatted using Markdown, as follows:
<A 2-3 line high-level summary>
#### Characters
<bullet list of characters and descriptions>
#### Summary
<bullet list of main events>py

--- DOCUMENT START ---
{file_content}
--- DOCUMENT END ---
"""

        # Print status messages to STDERR
        print(
            f"Processing {file_path} ({len(file_content)} characters)...",
            file=sys.stderr,
        )

        # --- 5. Get Summary and Print to STDOUT ---
        summary_text = get_gemini_summary(prompt)

        # Get the base file name without the .txt extension
        source_file_name = (
            os.path.basename(file_path).replace(".txt", "").replace("-", " ")
        )

        # Output to STDOUT in the requested format
        print(f"\n### {source_file_name}\n")
        print(summary_text)

        # sleep 1 minute between Gemini hits
        time.sleep(60)

    print("\n--- Summary Process Complete ---", file=sys.stderr)


def main():
    # --- 1. Take 2 integers as input command line parameters ---
    parser = argparse.ArgumentParser(
        description="Generate Gemini summaries for a range of 'Chapter-nn-*.txt' files."
    )
    parser.add_argument(
        "start_index", type=int, help="The starting chapter number (inclusive)."
    )
    parser.add_argument(
        "end_index", type=int, help="The ending chapter number (inclusive)."
    )
    args = parser.parse_args()

    # Check for API Key
    if not os.getenv("GEMINI_API_KEY"):
        print("FATAL: GEMINI_API_KEY environment variable not found.", file=sys.stderr)
        return

    if args.start_index > args.end_index:
        print(
            "Error: start_index must be less than or equal to end_index.",
            file=sys.stderr,
        )
        return

    # --- 2. Iterate and Process ---
    process_chapters(args.start_index, args.end_index)


if __name__ == "__main__":
    main()
