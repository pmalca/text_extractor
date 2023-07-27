# PDF Text Extractor

This repository contains a Python script that extracts text from PDF files and saves them as text files. The script utilizes the PyPDF2 library for reading PDF files and the langdetect library for language detection.

## Project Overview

The PDF Text Extractor performs the following steps:

1. **Data Input**: The script takes a directory path as input, which should contain PDF files to be processed.

2. **Text Extraction**: It reads each PDF file, extracts the text from each page, and concatenates it into a single string.

3. **Preprocessing**: The extracted text is converted to lowercase to standardize the text data.

4. **Language Detection**: The script performs language detection on the extracted text to determine the language of the content. It checks if the detected language is English before proceeding.

5. **Text Output**: If the detected language is English, the extracted text is saved as a separate text file in a specified output directory.

6. **Error Handling**: In case of any errors during the processing of files, the script displays an error message along with the filename and the specific error.

## Getting Started

To use the PDF Text Extractor, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Configure the input and output directories in the script to point to your desired directories.

4. Run the script using `python pdf_text_extractor.py`.

5. The extracted text will be saved as individual text files in the specified output directory.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to submit a pull request.
