import os
from PyPDF2 import PdfReader
from langdetect import detect

# Define input directory containing PDF files
pdf_dir = "D:/Decisiones de prueba/PDFs_prueba_3"

# Define output directory where extracted text files will be saved
output_dir = "D:/Decisiones de prueba/Txt.miner"

# Loop through each file in the PDF directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        try:
            # Open the PDF file in binary mode
            pdf_file = open(os.path.join(pdf_dir, filename), 'rb')
            
            # Create a PdfReader object to read the PDF file
            pdf_reader = PdfReader(pdf_file)
            
            # Initialize an empty string to store the extracted text
            text = ""
            
            # Iterate through each page in the PDF file
            for page_num in range(0, len(pdf_reader.pages)):
                # Extract text from the current page and append it to the 'text' variable
                text += pdf_reader.pages[page_num].extract_text()
            
            # Convert the extracted text to lowercase
            text = text.lower()
            
            # Perform language detection on the extracted text
            if detect(text) == 'en':
                # Generate a new file name by replacing the extension with '.txt'
                new_file_name = os.path.splitext(filename)[0] + ".txt"
                
                # Open a new text file in the output directory for writing
                with open(os.path.join(output_dir, new_file_name), "w", encoding="utf-8") as new_file:
                    # Write the extracted text to the new text file
                    new_file.write(text)
            
            # Close the PDF file
            pdf_file.close()
        
        except Exception as e:
            # If an error occurs during processing, print the error message and file name
            print("Error while processing file: ", filename)
            print("Error message: ", e)
