import requests

from src.config import WEATHER_API_KEY
from src.exceptions import WeatherAPIError


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(location:str) -> str:
    try:
        response = requests.get(
            BASE_URL,
            params={
                "q": location,
                "appid":WEATHER_API_KEY,
                "units":"metric",
            },
            timeout=10,
            )

        
        response.raise_for_status()
        return response.json()

    
    except requests.RequestException as exc :
        raise WeatherAPIError(
            "Failed to retrieve weather data."
        ) from exc




