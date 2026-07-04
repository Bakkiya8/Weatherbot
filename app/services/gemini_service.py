from google import genai
from google.genai import types
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.config.settings import GOOGLE_MODEL, GEMINI_API_KEY
from app.tools.weather_tool import get_weather  # registered as a tool


class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def chat(self, message: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=GOOGLE_MODEL,
                contents=[
                    SYSTEM_PROMPT,
                    message
                ],
                config=types.GenerateContentConfig(
                    tools=[get_weather]
                )
            )
            return response.text
        except Exception as e:
            raise RuntimeError(f"Gemini API call failed: {e}") from e