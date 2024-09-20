from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

logging.basicConfig(level=logging.INFO)

def split_text_documents(text_documents):
    """
    Splits text documents into chunks using RecursiveCharacterTextSplitter.
    
    Args:
        text_documents (list): List of text documents to be split.

    Returns:
        list: List of split documents.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=3600, chunk_overlap=100)
        documents = text_splitter.split_documents(text_documents)
        return documents
    except Exception as e:
        logging.error(f"Unexpected error splitting text documents: {e}")
        return []
