# -*- coding: utf-8 -*-
"""Weather widget views."""

import tkinter as tk
from dataclasses import dataclass
from typing import Callable

import overview.utils.formatters as fmt
from overview.models.weather import InstantForecast
from overview.views.shared.flexible import Flexible
from overview.views.shared.view import View


@dataclass
class CurrentWeatherViewProps:
    """Props for :class:`CurrentWeatherView`."""

    forecast: InstantForecast
    on_refresh: Callable[[], None]


class CurrentWeatherView(View[CurrentWeatherViewProps]):
    """View for current weather."""

    def _update(self):
        self.__real_temp.configure(
            text=fmt.format_temperature(self.props.forecast.real_temp)
        )
        self.__feels_like.configure(
            text="(" + fmt.format_temperature(self.props.forecast.feels_like_temp) + ")"
        )
        self.__weather_kind.configure(
            text=fmt.format_weather_kind(self.props.forecast.kind, with_desc=True)
        )
        self.__wind.configure(
            text=fmt.format_wind(
                self.props.forecast.wind_speed, self.props.forecast.wind_direction
            )
        )
        self.__refresh.configure(command=self.props.on_refresh)
        self.__humidity.configure(
            text=_("Humidity") + f": {self.props.forecast.humidity}%"
        )
        self.__pressure.configure(
            text=_("Pressure")
            + ": "
            + fmt.format_pressure(self.props.forecast.pressure)
        )

    def _render_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.__real_temp = Flexible(tk.Label)(
            self,
            anchor=tk.SE,
            font=("TkDefaultFont", 20),
        )
        self.__real_temp.grid(column=0, row=0)

        container = Flexible(tk.Frame)(self)
        container.grid(row=0, column=1, sticky="NEWS")
        self.__feels_like = Flexible(tk.Label)(
            container,
            anchor=tk.SW,
            font=("TkDefaultFont", 20),
            fg="#777777",
        )
        self.__feels_like.grid(row=0, column=0, sticky="NEWS")
        self.__refresh = tk.Button(container, text=_("Refresh"))
        self.__refresh.grid(row=0, column=1, sticky="SE")

        self.__weather_kind = Flexible(tk.Label)(
            self,
            anchor=tk.SE,
            font=("TkDefaultFont", 16),
        )
        self.__weather_kind.grid(row=1, column=0)
        self.__wind = Flexible(tk.Label)(
            self,
            anchor=tk.SW,
            font=("TkDefaultFont", 16),
        )
        self.__wind.grid(row=1, column=1)

        self.__humidity = Flexible(tk.Label)(self, anchor=tk.SE)
        self.__humidity.grid(row=2, column=0)
        self.__pressure = Flexible(tk.Label)(self, anchor=tk.SW)
        self.__pressure.grid(row=2, column=1)
