# -*- coding: utf-8 -*-
"""MVC controllers."""
from models.app import AppModel, WidgetKind
from views.app.app import AppView, AppViewProps
from views.app.app_bar import AppBarViewProps
from views.calendar.calendar import CalendarView
from views.notes.notes import NotesView
from views.weather.weather import WeatherView


class AppController:
    """Application controller (root controller)."""

    _title = "Overview"  # TODO: интернационализация

    def __init__(self, root):
        """Construct controller."""
        self.__model = AppModel(
            title=self._title,
            active_tab_index=0,
            tab_widgets=[WidgetKind.WEATHER, WidgetKind.CALENDAR, WidgetKind.NOTES],
        )
        self.__root = root
        self.__view = AppView(master=self.__root)
        self.__update_view()

    def __update_view(self):
        self.__view.update_props(
            AppViewProps(
                title=self.__model.title,
                app_bar=AppBarViewProps(
                    active_tab_index=self.__model.active_tab_index,
                    tabs=self.__model.tab_widgets,
                    on_activate_tab=self.__on_activate_tab,
                ),
            )
        )
        self.__view.set_child_view(self.__get_inner_view)

    def __get_inner_view(self, master):
        current_tab = self.__model.tab_widgets[self.__model.active_tab_index]

        if current_tab == WidgetKind.NOTES:
            return NotesView(master=master)
        elif current_tab == WidgetKind.WEATHER:
            return WeatherView(master=master)
        else:
            return CalendarView(master=master)

    def __on_activate_tab(self, tab_index: int):
        self.__model.active_tab_index = tab_index
        self.__update_view()

    def start(self):
        """Start application."""
        self.__root.mainloop()
