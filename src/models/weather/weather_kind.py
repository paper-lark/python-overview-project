# -*- coding: utf-8 -*-
"""Weather models."""
from enum import Enum


class WeatherKind(Enum):
    """Weather kinds."""

    SUNNY = 1
    RAINY = 2
    CLOUDY = 3
