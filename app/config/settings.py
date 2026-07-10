from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read Weather API Key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL")

#print(WEATHER_API_KEY)