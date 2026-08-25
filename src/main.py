import logging
from src.exceptions import ConfigurationError, WeatherAPIError
from src.services.weather_service import get_weather
from src.utils.validators import validate_location

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

def main():
    location = input("Enter a city: ")

    try:
        location = validate_location(location)

        weather = get_weather(location)

        print(f"\nWeather in {weather['name']}")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(
            f"Description: "
            f"{weather['weather'][0]['description']}"
        )

    except ValueError as exc:
        print(f"Input error: {exc}")

    except ConfigurationError as exc:
        print(f"Configuration error: {exc}")

    except WeatherAPIError as exc:
        print(f"Weather error: {exc}")


if __name__ == "__main__":
    main()