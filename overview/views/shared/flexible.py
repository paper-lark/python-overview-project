# -*- coding: utf-8 -*-
"""Flexible widget wrapper."""


def Flexible(cls):
    """Widget wrapper that makes widget flexible and applies basic grid layout."""

    class FlexibleWidget(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.grid(sticky="NEWS")
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)

    return FlexibleWidget
