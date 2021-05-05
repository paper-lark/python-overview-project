# -*- coding: utf-8 -*-
"""MVC controllers."""
import asyncio

from models.weather import WeatherModel
from utils.execution import run_in_background
from views.weather.weather import WeatherView, WeatherViewProps


class WeatherController:
    """Weather controller."""

    def __init__(self):
        """Construct controller."""
        self.__view = None
        self.model = WeatherModel()
        self._update_thread = None
        self._on_refresh()

    def create_view(self, master) -> WeatherView:
        """Create controlled view on the specified master widget."""
        self.__view = WeatherView(master=master)
        self._update_view()
        return self.__view

    def _on_refresh(self):
        if self._update_thread is not None and self._update_thread.is_alive():
            return
        self.model.is_loading = True
        self._update_view()
        self._update_thread = run_in_background(self._fetch_forecast())

    async def _fetch_forecast(self):
        loop = asyncio.get_event_loop()
        lat, lon = await loop.run_in_executor(None, self.model.fetch_geolocation)
        await loop.run_in_executor(None, lambda: self.model.fetch_forecast(lat, lon))
        self.model.is_loading = False
        self._update_view()

    def _update_view(self):
        if self.__view is not None:
            self.__view.update_props(
                WeatherViewProps(
                    forecast=self.model.forecast,
                    is_loading=self.model.is_loading,
                    on_refresh=self._on_refresh,
                )
            )
