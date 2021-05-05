# -*- coding: utf-8 -*-
"""Utils for text formatting."""
import datetime

from models.weather import WeatherKind

# TODO: интернациоанлизация


def format_temperature(temp: float) -> str:
    """Format temperature in Celcius."""
    return f"{int(temp)}℃"


def format_weather_kind(kind: WeatherKind, with_desc: bool = False) -> str:
    """Format weather kind."""
    if with_desc:
        return {
            WeatherKind.SUNNY: "Sunny ☀️",
            WeatherKind.RAIN: "Rainy ☔️",
            WeatherKind.CLOUDY: "Cloudy ☁️",
            WeatherKind.STORM: "Storm ⚡️",
            WeatherKind.DRIZZLE: "Drizzle ☔️",
            WeatherKind.SNOW: "Snow ❄️",
        }[kind]
    else:
        return {
            WeatherKind.SUNNY: "☀️",
            WeatherKind.RAIN: "☔️",
            WeatherKind.CLOUDY: "☁️",
            WeatherKind.STORM: "⚡️",
            WeatherKind.DRIZZLE: "☔️",
            WeatherKind.SNOW: "❄️",
        }[kind]


def format_time(t: datetime.time) -> str:
    """Format time."""
    return t.strftime("%H:%M")


def format_wind(speed: float, direction: float) -> str:
    """Format wind parameters."""
    return f"💨 {speed} m/s, {format_direction(direction)}"


def format_direction(direction_in_degrees: float) -> str:
    """Format direction given in degrees."""
    if direction_in_degrees <= 22.5 or direction_in_degrees > 337.5:
        return "N"
    elif direction_in_degrees <= 67.5:
        return "NE"
    elif direction_in_degrees <= 112.5:
        return "E"
    elif direction_in_degrees <= 157.5:
        return "SE"
    elif direction_in_degrees <= 202.5:
        return "S"
    elif direction_in_degrees <= 247.5:
        return "SW"
    elif direction_in_degrees <= 292.5:
        return "W"
    else:
        return "NW"
