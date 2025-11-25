#!/usr/bin/env python
import requests
import re
import os


def create_chapter_files():
    """
    Retrieves text from a URL, parses it into chapters, and saves each chapter
    to a separate file following the specified naming and content format.

    Gemini Prompt Used To Create This Script:
    -----------
    Please create a Python script which will:

    1) retrieve text from this URL

    https://www.loper-os.org/pub/warez/1st_circle.txt

    2) save the contents into separate files, one for each chapter, using the fact that:

    2.1) The start of each chapter is demarcated by a line containing only the word "Chapter" followed by a space and a positive integer.

    2.2) The line immediately following the "Chapter" line contains the chapter title.

    2.3) All lines until the start of the next chapter, or EOF, are the body of the chapter.

    3) Each output file should be named: Chapter-NN-XXXXXXXX.txt,
        where,
            NN = the chapter number
            XXXXXXXX = the chapter name, with spaces replaced by hyphens ("-")

    4) The contents of each output file should be:
            Chapter-NN-XXXXXXXX
            <blank line>
            <chapter contents>
    -----------

    """
    URL = "https://www.loper-os.org/pub/warez/1st_circle.txt"
    # Regex to identify a chapter line: "Chapter" followed by space and a positive integer,
    # ensuring it's the only content on the line.
    CHAPTER_PATTERN = re.compile(r"^Chapter (\d+)$")

    print(f"1) Retrieving text from: {URL}")
    # 1) Retrieve text from URL
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        text_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving content: {e}")
        return  # Exit if retrieval fails

    lines = text_content.splitlines()

    # Identify the line index for the start of every chapter ("Chapter NN")
    chapter_starts = [i for i, line in enumerate(lines) if CHAPTER_PATTERN.match(line)]

    print(f"Found {len(chapter_starts)} chapters. Processing and saving...")

    # 2) Save the contents into separate files
    for k, start_index in enumerate(chapter_starts):

        # --- 2.1 & 2.2: Extract Chapter Data ---

        # Chapter Line: e.g., "Chapter 1"
        chapter_line = lines[start_index]
        chapter_match = CHAPTER_PATTERN.match(chapter_line)

        # NN = the chapter number (zero-padded)
        nn = int(chapter_match.group(1))
        nn_str = f"{nn:02d}"

        # Chapter Title: line immediately following the "Chapter" line
        title = ""
        if start_index + 1 < len(lines):
            title = lines[start_index + 1].strip()
        else:
            title = f"Untitled Chapter {nn}"

            # Chapter Body: starts at start_index + 2
        body_start_index = start_index + 2

        # Body ends just before the next chapter's "Chapter NN" line, or at EOF.
        if k + 1 < len(chapter_starts):
            body_end_index = chapter_starts[k + 1]
        else:
            body_end_index = len(lines)

        body_lines = lines[body_start_index:body_end_index]
        # Join body lines back, preserving original spacing
        chapter_body = "\n".join(body_lines)

        # --- 3) File Naming ---

        # XXXXXXXX = chapter name, with spaces replaced by hyphens ("-")
        filename_title = title.strip().replace(" ", "-")

        filename = f"Chapter-{nn_str}-{filename_title}.txt"

        # --- 4) File Contents Format ---

        # Header: Chapter-NN-XXXXXXXX (The file's derived name without the extension)
        header_line = f"Chapter-{nn_str}-{filename_title}"

        # Contents: Header + blank line + chapter contents
        file_content = f"{header_line}\n\n{chapter_body}"

        # Save to file
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(file_content)
            print(f"Successfully created: {filename}")

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue  # Continue to the next chapter


if __name__ == "__main__":
    # Ensure the 'requests' library is installed: pip install requests
    create_chapter_files()
