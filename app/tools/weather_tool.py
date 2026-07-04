from app.services.weather_service import WeatherService

weather_service = WeatherService()


def get_weather(city: str):
    print(f"***** WEATHER TOOL CALLED ***** City: {city}")
    """
    Returns the current weather for a city.
    """

    return weather_service.get_weather(city)