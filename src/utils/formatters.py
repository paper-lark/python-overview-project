# -*- coding: utf-8 -*-
"""Utils for text formatting."""
import datetime

import babel.dates as dates
import babel.units as units

from models.weather import WeatherKind


def format_temperature(temp: float) -> str:
    """Format temperature in Celsius."""
    return units.format_unit(int(temp), "temperature-celsius", "short")


def format_weather_kind(kind: WeatherKind, with_desc: bool = False) -> str:
    """Format weather kind."""
    if with_desc:
        icon = format_weather_kind(kind)
        return {
            WeatherKind.SUNNY: _("Sunny") + " " + icon,
            WeatherKind.RAIN: _("Rainy") + " " + icon,
            WeatherKind.CLOUDY: _("Cloudy") + " " + icon,
            WeatherKind.STORM: _("Storm") + " " + icon,
            WeatherKind.DRIZZLE: _("Drizzle") + " " + icon,
            WeatherKind.SNOW: _("Snow") + " " + icon,
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
    return dates.format_time(t, format="hh:mm")


def format_wind(speed: float, direction: float) -> str:
    """Format wind parameters."""
    formatted_speed = units.format_unit(speed, "speed-meter-per-second", "short")
    return f"💨 {formatted_speed}, {format_direction(direction)}"


def format_pressure(pressure_in_pa: float) -> str:
    """Format pressure."""
    pressure_in_mm_hg = int(pressure_in_pa * 0.00750062)
    try:
        return units.format_unit(
            pressure_in_mm_hg, "pressure-millimeter-of-mercury", "short"
        )
    except units.UnknownUnitError:
        # NOTE: для русского языка нет перевода
        return str(pressure_in_mm_hg) + " " + _("mmHg")


def format_direction(direction_in_degrees: float) -> str:
    """Format direction given in degrees."""
    if direction_in_degrees <= 22.5 or direction_in_degrees > 337.5:
        return _("N")
    elif direction_in_degrees <= 67.5:
        return _("NE")
    elif direction_in_degrees <= 112.5:
        return _("E")
    elif direction_in_degrees <= 157.5:
        return _("SE")
    elif direction_in_degrees <= 202.5:
        return _("S")
    elif direction_in_degrees <= 247.5:
        return _("SW")
    elif direction_in_degrees <= 292.5:
        return _("W")
    else:
        return _("NW")


def format_day(day: datetime.date) -> str:
    """Format date."""
    return day.strftime("%d %b %Y")


def format_month_year(day: datetime.date) -> str:
    """Format date to get month and year only."""
    return day.strftime("%b %Y")


def format_day_string(day_string: str) -> datetime.date:
    """Format date string."""
    return datetime.datetime.strptime(day_string, "%d %b %Y").date()
