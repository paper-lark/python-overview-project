# -*- coding: utf-8 -*-


def Flexible(cls, sticky="NEWS"):
    class FlexibleWidget(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.grid(sticky=sticky)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)

    return FlexibleWidget
