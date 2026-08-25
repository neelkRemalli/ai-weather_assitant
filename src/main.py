from src.exceptions import WeatherAPIError
from src.services.weather_service import get_weather



def main():
    location = input("Enter a city: ").strip()

    if not location:
        print("Location can not be empty")
        return

    try:
        weather = get_weather(location)

        print(f"\nWeather in {weather["name"]}")
        print(f"Temperture: {weather["main"]["temp"]}°C")
        print(f"Description: {weather["weather"][0]["description"]}")
              

    except WeatherAPIError as exc:
        print(f"Error: {exc}")






if  __name__ == "__main__":

    main()

