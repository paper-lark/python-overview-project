# -*- coding: utf-8 -*-
"""Weather models."""
import datetime
from dataclasses import dataclass

from models.weather.weather_forecast_data import WeatherForecastData


@dataclass
class DailyForecastModel:
    """Model for daily weather forecast."""

    ts: datetime.date
    forecast: WeatherForecastData
