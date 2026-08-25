# AI Weather Assistant

A Python CLI application that retrieves current weather information
from OpenWeather and demonstrates clean API integration, validation,
error handling, testing, logging, and configuration management.

## Features

- Get current weather by city
- OpenWeather API integration
- Environment-based API configuration
- Input validation
- HTTP error handling
- Network and timeout handling
- JSON response validation
- Custom application exceptions
- Structured logging
- Automated tests with pytest
- Mocked API tests

## Requirements

- Python 3.12+
- OpenWeather API key
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-weather-assistant.git
cd ai-weather-assistant

## Wondows

python -m venv .venv

.venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Run  the app

python -m src.main

Enter a city: London


Weather in London

Temperature: 18.5°C

Description: clear sky

# Test the app

pytest

pytest -v


ai-weather-assistant/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── exceptions.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── weather_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── validators.py
│
├── tests/
│   ├── __init__.py
│   ├── test_weather_service.py
│   └── test_validators.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md



