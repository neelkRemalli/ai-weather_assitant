class WeatherAPIError(Exception):
    """Raised when the weather API request fails."""
    pass


class ConfigurationError(Exception):
    """Raised when required configuration is missing."""
    pass