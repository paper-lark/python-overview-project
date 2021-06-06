# -*- coding: utf-8 -*-
import datetime

import pytest
import pytz
import requests

import overview.models.weather as weather


class MockTextResponse(requests.Response):
    class ResponseData:
        def __init__(self, data: bytes):
            self.__data = data
            self.__ptr = 0

        def read(self, chunk_size):
            chunk = self.__data[self.__ptr : self.__ptr + chunk_size]
            self.__ptr += len(chunk)
            return chunk

    _text_encoding = "UTF-8"

    def __init__(self, data: str, status_code: int = 200):
        super().__init__()
        self.encoding = self._text_encoding
        self.raw = MockTextResponse.ResponseData(data.encode(self._text_encoding))
        self.status_code = status_code


@pytest.fixture
def coordinates():
    return 10, 20


@pytest.fixture
def weather_forecast_json():
    return """
    {
      "lat": 55.7522,
      "lon": 37.6156,
      "timezone": "Europe/Moscow",
      "timezone_offset": 10800,
      "current": {
        "dt": 1620414903,
        "sunrise": 1620351212,
        "sunset": 1620407917,
        "temp": 11,
        "feels_like": 9.2,
        "pressure": 1011,
        "humidity": 40,
        "dew_point": -1.83,
        "uvi": 0,
        "clouds": 0,
        "visibility": 10000,
        "wind_speed": 2,
        "wind_deg": 160,
        "weather": [
          {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
          }
        ]
      },
      "hourly": [
        {
          "dt": 1620414000,
          "temp": 11,
          "feels_like": 9.2,
          "pressure": 1011,
          "humidity": 40,
          "dew_point": -1.83,
          "uvi": 0,
          "clouds": 0,
          "visibility": 10000,
          "wind_speed": 4.53,
          "wind_deg": 183,
          "wind_gust": 11.52,
          "weather": [
            {
              "id": 800,
              "main": "Clear",
              "description": "clear sky",
              "icon": "01n"
            }
          ],
          "pop": 0
        },
        {
          "dt": 1620417600,
          "temp": 10.72,
          "feels_like": 8.97,
          "pressure": 1011,
          "humidity": 43,
          "dew_point": -1.18,
          "uvi": 0,
          "clouds": 20,
          "visibility": 10000,
          "wind_speed": 4.26,
          "wind_deg": 176,
          "wind_gust": 11.5,
          "weather": [
            {
              "id": 801,
              "main": "Clouds",
              "description": "few clouds",
              "icon": "02n"
            }
          ],
          "pop": 0
        }
      ],
      "daily": [
        {
          "dt": 1620378000,
          "sunrise": 1620351212,
          "sunset": 1620407917,
          "moonrise": 1620349140,
          "moonset": 1620389280,
          "moon_phase": 0.86,
          "temp": {
            "day": 12.56,
            "min": 5.36,
            "max": 14.04,
            "night": 10.72,
            "eve": 13.1,
            "morn": 5.85
          },
          "feels_like": {
            "day": 10.73,
            "night": 3.69,
            "eve": 11.41,
            "morn": 3.69
          },
          "pressure": 1011,
          "humidity": 33,
          "dew_point": -2.99,
          "wind_speed": 5.27,
          "wind_deg": 250,
          "wind_gust": 11.52,
          "weather": [
            {
              "id": 800,
              "main": "Clear",
              "description": "clear sky",
              "icon": "01d"
            }
          ],
          "clouds": 7,
          "pop": 0.08,
          "uvi": 4.08
        }
      ]
    }
    """


@pytest.fixture
def weather_forecast_dto():
    tz = pytz.timezone("Europe/Moscow")
    return weather.WeatherForecast(
        current=weather.InstantForecast(
            ts=tz.localize(datetime.datetime(2021, 5, 7, 22, 15, 3)),
            kind=weather.WeatherKind.SUNNY,
            real_temp=11.0,
            feels_like_temp=9.2,
            humidity=40,
            pressure=101100,
            wind_speed=2,
            wind_direction=160,
        ),
        hourly=[
            weather.InstantForecast(
                ts=tz.localize(datetime.datetime(2021, 5, 7, 22, 0)),
                kind=weather.WeatherKind.SUNNY,
                real_temp=11.0,
                feels_like_temp=9.2,
                humidity=40,
                pressure=101100,
                wind_speed=4,
                wind_direction=183,
            ),
            weather.InstantForecast(
                ts=tz.localize(datetime.datetime(2021, 5, 7, 23, 0)),
                kind=weather.WeatherKind.CLOUDY,
                real_temp=10.72,
                feels_like_temp=8.97,
                humidity=43,
                pressure=101100,
                wind_speed=4,
                wind_direction=176,
            ),
        ],
        daily=[
            weather.DailyForecast(
                ts=datetime.date(2021, 5, 7),
                kind=weather.WeatherKind.SUNNY,
                real_temp=weather.DailyTemperature(
                    morning=5.85, afternoon=12.56, evening=13.1, night=10.72
                ),
                feels_like_temp=weather.DailyTemperature(
                    morning=3.69, afternoon=10.73, evening=11.41, night=3.69
                ),
                humidity=33,
                pressure=101100,
                wind_speed=5,
                wind_direction=250,
            )
        ],
    )


@pytest.fixture
def mock_geolocation_request(mocker, coordinates):
    res = MockTextResponse(",".join(map(lambda c: str(c), coordinates)))
    m = mocker.patch("requests.get", return_value=res)
    return lambda: m.assert_called_once_with("https://ipinfo.io/loc")


@pytest.fixture
def mock_weather_request(mocker, coordinates, weather_forecast_json):
    res = MockTextResponse(weather_forecast_json)
    m = mocker.patch("requests.get", return_value=res)
    lat, lon = coordinates
    return lambda: m.assert_called_once_with(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}"
        + f"&lon={lon}&exclude=minutely,alerts&appid=9c7e7cac3d00697ac1bae5e5c88d4e99"
        + "&units=metric"
    )


def test_weather_model_should_fetch_forecast(
    mock_weather_request, weather_forecast_dto
):
    model = weather.WeatherModel()
    model.fetch_forecast(latitude=10, longitude=20)
    actual = model.forecast

    mock_weather_request()
    assert actual == weather_forecast_dto


def test_weather_model_should_fetch_geolocation(mock_geolocation_request, coordinates):
    model = weather.WeatherModel()
    lat, lon = model.fetch_geolocation()

    mock_geolocation_request()
    assert lat, lon == coordinates
