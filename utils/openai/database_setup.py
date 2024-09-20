import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import logging

logging.basicConfig(level=logging.INFO)

def create_directory_if_not_exists(directory_path):
    """
    Creates a directory if it does not exist.
    
    Args:
        directory_path (str): Path to the directory to be created.
    """
    try:
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory {directory_path} created.")
        else:
            logging.info(f"Directory {directory_path} already exists.")
    except OSError as e:
        logging.error(f"OS error while creating directory {directory_path}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while creating directory {directory_path}: {e}")

def setup_database(documents, directory):
    """
    Set up the Chroma database with the given documents.
    
    Args:
        documents (list): List of documents to be added to the database.
        directory (str): Path to the directory where the database will be stored.

    Returns:
        Chroma: An instance of the Chroma vector store.
    """
    try:
        if not documents:
            raise ValueError("No documents provided for database setup.")
        
        # Create the directory if it does not exist
        create_directory_if_not_exists(directory)
        
        db = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings(), persist_directory=directory)
        return db
    except ValueError as e:
        logging.error(f"Value error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error setting up database: {e}")
    return None
