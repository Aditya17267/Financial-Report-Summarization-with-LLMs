import os

def create_file_if_not_exists(file_path):
    """
    Creates an empty file if it does not exist.
    
    Args:
        file_path (str): Path to the file to be created.
    """
    try:
        if not os.path.isfile(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                # Just create an empty file
                pass
            print(f"File {file_path} created.")
        else:
            print(f"File {file_path} already exists.")
    except IOError:
        print(f"IO error while creating file {file_path}.")
    except Exception as e:
        print(f"Unexpected error while creating file {file_path}: {e}")

def get_paths():
    """
    Get file paths for PDFs and outputs from user input.
    
    Returns:
        tuple: Contains paths for PDF directory, output text file, output DOCX file, and vector DB directory.
    """
    try:
        print("Pls ensure that you are entering the complete path for the required directories \n For the extracted text file and the output docx file you can enter either the file path or a directory path.\n")
        pdf_directory = input("Enter the path to the input PDF directory: ")
        if not os.path.isdir(pdf_directory):
            raise FileNotFoundError(f"PDF directory {pdf_directory} does not exist.")
        
        
        output_text_file = input("Enter the path to store the extracted text from pdf files: ")

        if(".txt" not in output_text_file):
            output_text_file += '/extracted_text.txt'
            create_file_if_not_exists(output_text_file)
        
        output_docx_file = input("Enter the path for storing 2 page output DOCX file: ")
        output_1_pager = input("Enter the path for storing 1 page output DOCX file: ")
        vector_db_directory = 'vector_db'
                
        return pdf_directory, output_text_file, output_docx_file, output_1_pager, vector_db_directory
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return None, None, None, None
    except Exception as e:
        print(f"Unexpected error getting paths: {e}")
        return None, None, None, None
