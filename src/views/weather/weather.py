# -*- coding: utf-8 -*-
"""Weather widget views."""
from dataclasses import dataclass
from typing import Callable

from models.weather import WeatherForecast
from views.shared.view import View
from views.weather.current_weather import CurrentWeatherView, CurrentWeatherViewProps
from views.weather.today_weather import TodayWeatherView, TodayWeatherViewProps


@dataclass
class WeatherViewProps:
    """Props for weather view."""

    forecast: WeatherForecast
    on_refresh: Callable[[], None]


class WeatherView(View[WeatherViewProps]):
    """View for weather screen."""

    def _update(self):
        self.__current.update_props(
            CurrentWeatherViewProps(
                forecast=self.props.forecast.current,
                on_refresh=self.props.on_refresh,
            )
        )
        self.__today.update_props(
            TodayWeatherViewProps(forecasts=self.props.forecast.hourly)
        )

    def _render_widgets(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.__current = CurrentWeatherView(self)
        self.__current.grid(row=0, column=0, sticky="NS")
        self.__today = TodayWeatherView(self)
        self.__today.grid(row=1, column=0, sticky="NEWS")
