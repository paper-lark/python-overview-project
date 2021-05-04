# -*- coding: utf-8 -*-
"""Weather models."""
import datetime
from dataclasses import dataclass

from models.weather.weather_forecast_data import WeatherForecastData


@dataclass
class HourlyForecastModel:
    """Model for hourly weather forecast."""

    ts: datetime.datetime
    forecast: WeatherForecastData
