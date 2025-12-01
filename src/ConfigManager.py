import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """
    Centralized configuration management.
    Updated for Google Gemini support.
    """
    
    # Switch to Google API Key
    API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Default to a Gemini model (Flash is fast and cheap)
    MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    
    # Enterprise Practice: Fail Fast
    if not API_KEY:
        raise ValueError(
            " CRITICAL ERROR: GOOGLE_API_KEY not found in environment variables.\n"
            "   Please ensure you have created a .env file with your Gemini key."
        )

# Create singleton
settings = Config()