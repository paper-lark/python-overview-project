# -*- coding: utf-8 -*-
import datetime
from dataclasses import dataclass

from models.weather.weather_forecast_data import WeatherForecastData


@dataclass
class DailyForecastModel:
    ts: datetime.date
    forecast: WeatherForecastData
