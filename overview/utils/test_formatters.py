import datetime

import pytest

import overview.utils.formatters as fmt
from overview.models.weather import WeatherKind


@pytest.mark.parametrize(
    "direction,expected",
    [
        (0, "N"),
        (90, "E"),
        (180, "S"),
        (270, "W"),
        (45, "NE"),
        (135, "SE"),
        (225, "SW"),
        (315, "NW"),
    ],
)
def test_format_direction(direction, expected):
    assert fmt.format_direction(direction) == expected


def test_format_pressure():
    assert fmt.format_pressure(pressure_in_pa=1000) == "7 mmHg"


def test_format_wind():
    assert fmt.format_wind(speed=10.3, direction=90) == "💨 10.3 m/s, E"


@pytest.mark.parametrize(
    "kind,expected",
    [
        (WeatherKind.SUNNY, "☀️"),
        (WeatherKind.RAIN, "☔️"),
        (WeatherKind.CLOUDY, "☁️"),
        (WeatherKind.STORM, "⚡️"),
        (WeatherKind.DRIZZLE, "☔️"),
        (WeatherKind.SNOW, "❄️"),
    ],
)
def test_format_weather_kind_short(kind, expected):
    assert fmt.format_weather_kind(kind) == expected


@pytest.mark.parametrize(
    "kind,expected",
    [
        (WeatherKind.SUNNY, "Sunny ☀️"),
        (WeatherKind.RAIN, "Rainy ☔️"),
        (WeatherKind.CLOUDY, "Cloudy ☁️"),
        (WeatherKind.STORM, "Storm ⚡️"),
        (WeatherKind.DRIZZLE, "Drizzle ☔️"),
        (WeatherKind.SNOW, "Snow ❄️"),
    ],
)
def test_format_weather_kind_with_description(kind, expected):
    assert fmt.format_weather_kind(kind, with_desc=True) == expected


def test_format_time():
    assert fmt.format_time(datetime.time(hour=10, minute=20, second=30)) == "10:20"


def test_format_temperature():
    assert fmt.format_temperature(20.32) == "20°C"
