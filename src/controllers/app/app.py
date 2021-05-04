# -*- coding: utf-8 -*-
from views.app.app import AppView


class AppController:
    _title = "Overview"  # TODO: интернационализация

    def __init__(self, parent):
        self.view = AppView(parent, self._title)

    def mainloop(self):
        self.view.mainloop()
