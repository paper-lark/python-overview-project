# -*- coding: utf-8 -*-
"""Weather models."""
from __future__ import annotations

import datetime
import enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import requests


class WeatherKind(enum.Enum):
    """Weather kinds."""

    SUNNY = 1
    RAIN = 2
    CLOUDY = 3
    STORM = 4
    DRIZZLE = 5
    SNOW = 6

    @staticmethod
    def from_api(weather_id: int) -> WeatherKind:
        """Parse weather kind from ID received from API.

        Read more: https://openweathermap.org/weather-conditions

        :param weather_id: weather kind ID
        :return: weather kind
        """
        if weather_id < 300:
            return WeatherKind.STORM
        elif weather_id < 400:
            return WeatherKind.DRIZZLE
        elif weather_id < 600:
            return WeatherKind.RAIN
        elif weather_id < 700:
            return WeatherKind.SNOW
        elif weather_id == 800:
            return WeatherKind.SUNNY
        else:
            return WeatherKind.CLOUDY


@dataclass
class InstantForecast:
    """Weather forecast at specified time point."""

    ts: datetime.datetime
    kind: WeatherKind
    real_temp: float
    feels_like_temp: float
    humidity: int
    pressure: int  # in Pa
    wind_speed: int
    wind_direction: int

    @staticmethod
    def from_api(obj: Dict) -> InstantForecast:
        """Parse forecast data from API response.

        Read more: https://openweathermap.org/api/one-call-api#parameter

        :param obj: weather JSON object
        :return: forecast data
        """
        return InstantForecast(
            ts=datetime.datetime.fromtimestamp(obj["dt"]),
            kind=WeatherKind.from_api(int(obj["weather"][0]["id"])),
            real_temp=float(obj["temp"]),
            feels_like_temp=float(obj["feels_like"]),
            humidity=int(obj["humidity"]),
            pressure=int(obj["pressure"]) * 100,
            wind_speed=int(obj["wind_speed"]),
            wind_direction=int(obj["wind_deg"]),
        )


@dataclass
class DailyTemperature:
    """Daily forecasted temperatures."""

    morning: float
    afternoon: float
    evening: float
    night: float

    @staticmethod
    def from_api(obj: Dict) -> DailyTemperature:
        """Parse daily temperatures from API response.

        Read more: https://openweathermap.org/api/one-call-api#parameter

        :param obj: daily temperatures JSON object
        :return: forecast data
        """
        return DailyTemperature(
            morning=float(obj["morn"]),
            afternoon=float(obj["day"]),
            evening=float(obj["eve"]),
            night=float(obj["night"]),
        )


@dataclass
class DailyForecast:
    """Daily weather forecast."""

    ts: datetime.date
    kind: WeatherKind
    real_temp: DailyTemperature
    feels_like_temp: DailyTemperature
    humidity: int
    pressure: int  # in Pa
    wind_speed: int
    wind_direction: int

    @staticmethod
    def from_api(obj: Dict) -> DailyForecast:
        """Parse forecast from API response.

        Read more: https://openweathermap.org/api/one-call-api#parameter

        :param obj: weather JSON object
        :return: forecast data
        """
        return DailyForecast(
            ts=datetime.date.fromtimestamp(obj["dt"]),
            real_temp=DailyTemperature.from_api(obj["temp"]),
            feels_like_temp=DailyTemperature.from_api(obj["feels_like"]),
            kind=WeatherKind.from_api(int(obj["weather"][0]["id"])),
            humidity=int(obj["humidity"]),
            pressure=int(obj["pressure"]) * 100,
            wind_speed=int(obj["wind_speed"]),
            wind_direction=int(obj["wind_deg"]),
        )


@dataclass
class WeatherForecast:
    """Model for weather controller."""

    current: InstantForecast
    hourly: List[InstantForecast]
    daily: List[DailyForecast]


class WeatherModel:
    """Model for working with weather forecast."""

    __api_key = "9c7e7cac3d00697ac1bae5e5c88d4e99"

    def __init__(self):
        """Construct model."""
        self.forecast: Optional[WeatherForecast] = None
        self.is_loading = False

    def fetch_forecast(self, latitude: float, longitude: float):
        """Get forecast."""
        print(f"Fetching weather forecast for ({latitude}, {longitude})")
        res = requests.get(self.__get_url(longitude, latitude))
        res.raise_for_status()
        result = res.json()

        # TODO: написать тесты на парсеры ответа API
        self.forecast = WeatherForecast(
            current=InstantForecast.from_api(result["current"]),
            hourly=list(
                map(lambda obj: InstantForecast.from_api(obj), result["hourly"])
            ),
            daily=list(map(lambda obj: DailyForecast.from_api(obj), result["daily"])),
        )

    def fetch_geolocation(self) -> Tuple[float, float]:
        """Get current geolocation.

        :return: tuple with latitude and longitude.
        """
        print("Fetching geolocation")
        res = requests.get("https://ipinfo.io/loc")
        lat, lon = map(lambda x: float(x), res.text.split(","))
        return lat, lon

    def __get_url(self, longitude, latitude):
        return (
            f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}"
            + f"&lon={longitude}&exclude=minutely,alerts&appid={self.__api_key}"
            + "&units=metric"
        )
