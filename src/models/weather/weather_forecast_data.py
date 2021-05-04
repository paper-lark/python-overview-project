# -*- coding: utf-8 -*-
from dataclasses import dataclass

from models.weather.weather_kind import WeatherKind


@dataclass
class WeatherForecastData:
    kind: WeatherKind
    real_temp: float
    feels_like_temp: float
    humidity: int
    pressure: int
    wind_speed: int
    wind_direction: int
