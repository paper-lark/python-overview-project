# -*- coding: utf-8 -*-


def Flexible(cls):
    class FlexibleWidget(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.grid(sticky="NEWS")
            self.columnconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)

    return FlexibleWidget
