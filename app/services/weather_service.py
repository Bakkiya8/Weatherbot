import httpx #call external API
from app.config.settings import WEATHER_API_KEY


class WeatherService:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather" #OpenWeather endpoint

    def get_weather(self, city: str):

        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }

        response = httpx.get(self.BASE_URL, params=params)

       # return response.json()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
            }