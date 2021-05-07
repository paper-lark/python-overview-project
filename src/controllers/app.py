# -*- coding: utf-8 -*-
"""MVC controllers."""
from controllers.weather import WeatherController
from models.app import AppModel, WidgetKind
from views.app.app import AppView, AppViewProps
from views.app.app_bar import AppBarViewProps
from views.calendar.calendar import CalendarView
from views.notes.notes import NotesView


class AppController:
    """Application controller (root controller)."""

    _title = "Overview"

    def __init__(self, root):
        """Construct controller."""
        self.model = AppModel(
            title=self._title,
            active_tab_index=0,
            tab_widgets=[WidgetKind.WEATHER, WidgetKind.CALENDAR, WidgetKind.NOTES],
        )
        self.__root = root
        self.__root.minsize(200, 400)
        self.view = AppView(master=self.__root)
        self._weather_vc = WeatherController()
        self.__update_view()

    def __update_view(self):
        self.view.update_props(
            AppViewProps(
                title=self.model.title,
                app_bar=AppBarViewProps(
                    active_tab_index=self.model.active_tab_index,
                    tabs=self.model.tab_widgets,
                    on_activate_tab=self.__on_activate_tab,
                ),
            )
        )
        self.view.set_child_view(self.__get_inner_view)

    def __get_inner_view(self, master):
        current_tab = self.model.tab_widgets[self.model.active_tab_index]

        if current_tab == WidgetKind.NOTES:
            return NotesView(master=master)
        elif current_tab == WidgetKind.WEATHER:
            return self._weather_vc.create_view(master=master)
        else:
            return CalendarView(master=master)

    def __on_activate_tab(self, tab_index: int):
        self.model.active_tab_index = tab_index
        self.__update_view()

    def start(self):
        """Start application."""
        self.__root.mainloop()
