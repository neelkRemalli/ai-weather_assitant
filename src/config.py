import os
from dotenv import load_dotenv


load_dotenv()


def get_weather_api_key() -> str:
    api_key = os.getenv("WEATHER_API_KEY")


    if not api_key:
        raise ChildProcessError(
            "WEATHER_API_KEY is not configured."
        )


    return api_key





# openai/gpt-oss-20b:free
# WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
# OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

