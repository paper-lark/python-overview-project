# -*- coding: utf-8 -*-
"""Weather models."""
from dataclasses import dataclass
from typing import List

from models.weather.daily_forecast_model import DailyForecastModel
from models.weather.hourly_forecast_model import HourlyForecastModel


@dataclass
class WeatherForecastModel:
    """Model for weather controller."""

    hourly: List[HourlyForecastModel]
    daily: List[DailyForecastModel]
