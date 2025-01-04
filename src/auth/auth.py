from dotenv import load_dotenv
import os

def authentication():
    load_dotenv()
    return os.getenv('API_KEY')