import os
from dotenv import load_dotenv

def load_config():
    """Load environment variables and configurations"""
    load_dotenv()
    return os.getenv("GROQ_API_KEY")
