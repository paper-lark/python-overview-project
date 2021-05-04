# -*- coding: utf-8 -*-
"""MVC controllers."""
from models.app.app import AppModel
from models.app.widget_kind import WidgetKind
from views.app.app import AppView, AppViewProps
from views.app.app_bar import AppBarViewProps


class AppController:
    """Application controller (root controller)."""

    _title = "Overview"  # TODO: интернационализация

    def __init__(self, parent):
        """Construct controller."""
        self.__model = AppModel(
            title=self._title,
            active_tab_index=0,
            tab_widgets=[WidgetKind.WEATHER, WidgetKind.CALENDAR, WidgetKind.NOTES],
        )
        self.__parent = parent
        self.__view = None
        self.__create_view()

    def __create_view(self):
        if self.__view is not None:
            self.__view.destroy()
        self.__view = AppView(
            self.__parent,
            AppViewProps(
                title=self.__model.title,
                app_bar=AppBarViewProps(
                    active_tab_index=self.__model.active_tab_index,
                    tabs=self.__model.tab_widgets,
                    on_activate_tab=self.__on_activate_tab,
                ),
            ),
        )

    def __on_activate_tab(self, tab_index: int):
        print(f"Active tab: {tab_index}")
        self.__model.active_tab_index = tab_index
        self.__create_view()  # TODO: refactor update mechanism

    def start(self):
        """Start application."""
        self.__view.mainloop()
