import pytest
import requests

from src.exceptions import WeatherAPIError
from src.services import weather_service


class MockWeatherResponse:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {
            "name": "London",
            "main": {
                "temp": 18.5,
            },
            "weather": [
                {
                    "description": "clear sky",
                }
            ],
        }


def test_get_weather(monkeypatch):
    monkeypatch.setattr(
        weather_service.requests,
        "get",
        lambda *args, **kwargs: MockWeatherResponse(),
    )

    weather = weather_service.get_weather("London")

    assert weather["name"] == "London"
    assert "main" in weather
    assert "weather" in weather


def test_invalid_city(monkeypatch):
    class MockResponse:
        status_code = 404

        def raise_for_status(self):
            raise requests.HTTPError(
                "404 Client Error"
            )

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        lambda *args, **kwargs: MockResponse(),
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("UnknownCity")


def test_invalid_api_key(monkeypatch):
    class MockResponse:
        status_code = 401

        def raise_for_status(self):
            raise requests.HTTPError(
                "401 Client Error"
            )

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        lambda *args, **kwargs: MockResponse(),
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("London")


def test_connection_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError(
            "Connection failed"
        )

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        mock_get,
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("London")


def test_timeout(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.Timeout(
            "Request timed out"
        )

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        mock_get,
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("London")


def test_malformed_json(monkeypatch):
    class MockResponse:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            raise ValueError("Invalid JSON")

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        lambda *args, **kwargs: MockResponse(),
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("London")


def test_incomplete_weather_response(monkeypatch):
    class MockResponse:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "name": "London",
            }

    monkeypatch.setattr(
        weather_service.requests,
        "get",
        lambda *args, **kwargs: MockResponse(),
    )

    with pytest.raises(WeatherAPIError):
        weather_service.get_weather("London")