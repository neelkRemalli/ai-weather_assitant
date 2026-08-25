import logging

import requests

from src.config import get_weather_api_key
from src.exceptions import WeatherAPIError


logger = logging.getLogger(__name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def _validate_weather_data(data: dict) -> dict:
    if not isinstance(data, dict):
        raise WeatherAPIError(
            "Weather service returned invalid data."
        )

    required_fields = {"name", "main", "weather"}

    if not required_fields.issubset(data):
        raise WeatherAPIError(
            "Weather service returned incomplete data."
        )

    return data


def get_weather(location: str) -> dict:
    api_key = get_weather_api_key()

    logger.info(
        "Fetching weather for location: %s",
        location,
    )

    try:
        response = requests.get(
            BASE_URL,
            params={
                "q": location,
                "appid": api_key,
                "units": "metric",
            },
            timeout=10,
        )

        response.raise_for_status()

        try:
            data = response.json()

        except ValueError as exc:
            raise WeatherAPIError(
                "Weather service returned invalid JSON."
            ) from exc

        return _validate_weather_data(data)

    except requests.HTTPError as exc:
        logger.error(
            "Weather API HTTP error: %s",
            exc,
        )

        if response.status_code == 401:
            raise WeatherAPIError(
                "Invalid weather API key."
            ) from exc

        if response.status_code == 404:
            raise WeatherAPIError(
                "City not found."
            ) from exc

        raise WeatherAPIError(
            "Weather service returned an HTTP error."
        ) from exc

    except requests.RequestException as exc:
        logger.error(
            "Weather API request failed: %s",
            exc,
        )

        raise WeatherAPIError(
            "Failed to connect to the weather service."
        ) from exc