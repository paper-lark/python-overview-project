# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List

from models.weather.daily_forecast_model import DailyForecastModel
from models.weather.hourly_forecast_model import HourlyForecastModel


@dataclass
class WeatherForecastModel:
    hourly: List[HourlyForecastModel]
    daily: List[DailyForecastModel]
