# -*- coding: utf-8 -*-
"""Weather widget views."""
from dataclasses import dataclass
from tkinter import ttk
from typing import Callable, Optional

from overview.models.weather import WeatherForecast
from overview.views.shared.flexible import Flexible
from overview.views.shared.loading import LoadingScreen
from overview.views.shared.view import View
from overview.views.weather.current_weather import (
    CurrentWeatherView,
    CurrentWeatherViewProps,
)
from overview.views.weather.today_weather import TodayWeatherView, TodayWeatherViewProps


@dataclass
class WeatherViewProps:
    """Props for weather view."""

    is_loading: bool
    forecast: Optional[WeatherForecast]
    on_refresh: Callable[[], None]


class WeatherView(View[WeatherViewProps]):
    """View for weather screen."""

    def _update(self):
        if self.props.is_loading or self.props.forecast is None:
            self.__loading.start()
            self.__loading.lift()
            return

        self.__current.update_props(
            CurrentWeatherViewProps(
                forecast=self.props.forecast.current,
                on_refresh=self.props.on_refresh,
            )
        )
        self.__today.update_props(
            TodayWeatherViewProps(forecasts=self.props.forecast.hourly)
        )
        self.__loading.stop()
        self.__loading.lower()

    def _render_widgets(self):
        self.__container = Flexible(ttk.Frame)(self)
        self.__container.grid(row=0, column=0)
        self.__container.rowconfigure(0, weight=0)
        self.__container.rowconfigure(1, weight=1)
        self.__current = CurrentWeatherView(self.__container)
        self.__current.grid(row=0, column=0, pady=8, sticky="NS")
        self.__today = TodayWeatherView(self.__container)
        self.__today.grid(row=1, column=0, pady=8, sticky="NEWS")

        self.__loading = LoadingScreen(master=self)
        self.__loading.grid(row=0, column=0)
