import os
import glob
from .pdf_extraction import extract_text_from_pdf
import logging

logging.basicConfig(level=logging.INFO)

def process_pdfs(pdf_directory, output_file):
    """
    Processes all PDF files in a directory and saves the extracted text to a file.
    
    Args:
        pdf_directory (str): Directory containing the PDF files.
        output_file (str): Path to the output file where extracted text will be saved.
    """
    try:
        if not os.path.isdir(pdf_directory):
            raise FileNotFoundError(f"PDF directory {pdf_directory} does not exist.")
        
        pdf_paths = glob.glob(os.path.join(pdf_directory, '*.pdf'))
        if not pdf_paths:
            raise FileNotFoundError(f"No PDF files found in directory {pdf_directory}.")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for pdf_path in pdf_paths:
                filename = os.path.basename(pdf_path)
                logging.info(f'\nExtracting text from file: {filename}')
                text_data = extract_text_from_pdf(pdf_path)
                f.write(f'\n\n{filename}\n{text_data}')
                logging.info(f'Extracted text from {pdf_path}')
        logging.info(f'\nAll extracted text has been saved to {output_file}')
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
    except IOError:
        logging.error(f"IO error while writing to {output_file}.")
    except Exception as e:
        logging.error(f"Unexpected error processing PDFs: {e}")
