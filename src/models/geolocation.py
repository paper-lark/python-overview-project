# -*- coding: utf-8 -*-
from typing import Tuple

import requests


class GeolocationModel:
    def fetch_geolocation(self) -> Tuple[float, float]:
        res = requests.get('https://ipinfo.io/loc')
        lat, lon = map(lambda x: float(x), res.text.split(','))
        return lat, lon
