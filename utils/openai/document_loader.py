from langchain_community.document_loaders import TextLoader
import os
import logging

logging.basicConfig(level=logging.INFO)

def load_documents(file_path):
    """
    Load text documents from a file.
    
    Args:
        file_path (str): Path to the text file.

    Returns:
        list: List of documents loaded from the file.
    """
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        
        loader = TextLoader(file_path, encoding='utf-8')
        return loader.load()
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
        return []
    except IOError:
        logging.error(f"IO error while reading file {file_path}.")
        return []
    except Exception as e:
        logging.error(f"Unexpected error loading documents from {file_path}: {e}")
        return []
