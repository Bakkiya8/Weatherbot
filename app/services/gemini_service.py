from google import genai
from google.genai import types
from google.genai import errors as genai_errors
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.config.settings import GOOGLE_MODEL, GEMINI_API_KEY
from app.tools.weather_tool import get_weather  # registered as a tool
from fastapi import HTTPException


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
        
        except genai_errors.APIError as e:
            status_code = getattr(e, "code", None) or 500
            message_detail = getattr(e, "message", str(e))

            if status_code == 503:
                raise HTTPException(
                    status_code=503,
                    detail="Gemini service is temporarily unavailable due to high demand. Please try again in a few minutes.",
                ) from e
            elif status_code == 429:
                raise HTTPException(
                    status_code=429,
                    detail="Gemini API quota exceeded. Please wait for the quota to reset or use another API key.",
                ) from e
            elif status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail=f"The configured Gemini model '{GOOGLE_MODEL}' was not found. Please verify the model name.",
                ) from e
            elif status_code == 401:
                raise HTTPException(
                    status_code=401,
                    detail="Gemini authentication failed. Please verify your API key.",
                ) from e
            else:
                raise HTTPException(
                    status_code=status_code if isinstance(status_code, int) else 500,
                    detail=f"Unexpected Gemini API error: {message_detail}",
                ) from e

        except Exception as e:
            # Catch-all for non-API errors (network issues, bad SDK config, etc.)
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected server error while contacting Gemini: {str(e)}",
            ) from e