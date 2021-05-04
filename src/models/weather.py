# -*- coding: utf-8 -*-
"""Weather models."""
import datetime
import enum
from dataclasses import dataclass
from typing import List


class WeatherKind(enum.Enum):
    """Weather kinds."""

    SUNNY = 1
    RAINY = 2
    CLOUDY = 3


@dataclass
class ForecastData:
    """Weather forecast description."""

    kind: WeatherKind
    real_temp: float
    feels_like_temp: float
    humidity: int
    pressure: int
    wind_speed: int
    wind_direction: int


@dataclass
class DailyForecast:
    """Model for daily weather forecast."""

    ts: datetime.date
    forecast: ForecastData


@dataclass
class HourlyForecast:
    """Model for hourly weather forecast."""

    ts: datetime.datetime
    forecast: ForecastData


@dataclass
class WeatherForecast:
    """Model for weather controller."""

    hourly: List[HourlyForecast]
    daily: List[DailyForecast]


class WeatherForecastModel:
    """Model for working with weather forecast."""

    def get_forecast(self) -> WeatherForecast:
        """Get forecast."""
        return WeatherForecast(hourly=[], daily=[])
