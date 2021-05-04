# -*- coding: utf-8 -*-
"""MVC controllers."""
from models.geolocation import GeolocationModel
from models.weather import WeatherModel
from views.weather.weather import WeatherView, WeatherViewProps


class WeatherController:
    """Weather controller."""

    def __init__(self):
        """Construct controller."""
        self.__view = None
        self.model = WeatherModel()
        self._geo_model = GeolocationModel()
        lat, lon = self._geo_model.fetch_geolocation()
        self.model.fetch_forecast(lat, lon)
        # FIXME: load data asynchronously async

    def create_view(self, master) -> WeatherView:
        """Create controlled view on the specified master widget."""
        self.__view = WeatherView(master=master)
        self._update_view()
        return self.__view

    def _on_refresh(self):
        lat, lon = self._geo_model.fetch_geolocation()
        self.model.fetch_forecast(lat, lon)
        self._update_view()

    def _update_view(self):
        if self.__view is not None:
            self.__view.update_props(
                WeatherViewProps(
                    forecast=self.model.forecast,
                    on_refresh=self._on_refresh
                )
            )

