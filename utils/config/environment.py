import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

def load_environment():
    """
    Load environment variables from a .env file.
    """
    try:
        load_dotenv()
        if not os.getenv('OPENAI_API_KEY'):
            raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    except EnvironmentError as e:
        logging.error(f"Environment error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error loading environment variables: {e}")
