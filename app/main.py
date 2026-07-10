from fastapi import FastAPI
from app.services.weather_service import WeatherService
from app.services.gemini_service import GeminiService
from app.models.chat import ChatRequest
import traceback


# Create a FastAPI application
app = FastAPI()
weather_service = WeatherService()
gemini_service = GeminiService()



# Root endpoint
# Decorator - When someone sends a GET request to /, execute the function below
@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Weather Bot!",
        "date": "29-06"
    }
    

@app.get("/weather")
def get_weather(city: str):
    return weather_service.get_weather(city)
    # return { 
    #     "city": city,
    #     "temperature": "25°C",
    #     "condition": "Sunny"
         
    # }

@app.post("/chat")
def chat(request: ChatRequest):
    response = gemini_service.chat(request.message)

    return {
        "reply": response
    }
