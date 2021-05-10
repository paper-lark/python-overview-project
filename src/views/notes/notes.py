# -*- coding: utf-8 -*-
"""Notes widget views."""
import datetime
import tkinter as tk
from collections import OrderedDict
from dataclasses import dataclass

from views.shared.flexible import Flexible
from views.shared.scrollable import Scrollable
from views.shared.view import View


@dataclass
class NoteViewProps:
    """Props for note view."""

    id: int
    title: str
    text: str
    creationTime: datetime.datetime
    lastChangeTime: datetime.datetime


@dataclass
class NotesViewProps:
    """Props for all notes view."""

    notesDict: OrderedDict


class CurrentNote(View[NoteViewProps]):
    """View for opened note."""

    def disable(self):
        """Disable title and tetx of note, if there are no existing notes."""
        self.title.grid_remove()
        self.text.grid_remove()

    def _update(self):
        self.title.grid()
        self.text.grid()
        self.title.delete("0", "end")
        self.title.insert("0", self.props.title)
        self.text.delete("1.0", "end")
        self.text.insert("1.0", self.props.text[:-1])

    def _render_widgets(self):
        self.title = Flexible(tk.Entry)(self)
        self.text = Flexible(tk.Text)(self)
        self.title.grid(row=0, column=0, sticky="NEWS")
        self.text.grid(row=1, column=0, sticky="NEWS")
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)


class NoteHeader(View[NoteViewProps]):
    """View for note in scrollable view."""

    def _update(self):
        self._title.configure(text=self.props.title)
        self._lastChangeTime.configure(text=self.props.lastChangeTime)

    def _render_widgets(self):
        self._title = Flexible(tk.Label)(self)
        self._lastChangeTime = Flexible(tk.Label)(self)

        self._title.grid(row=0, column=0, sticky="NEWS")
        self._lastChangeTime.grid(row=1, column=0, sticky="NEWS")


class NotesView(View[NotesViewProps]):
    """View for notes screen."""

    def _update(self):
        for header in self._notesHeaders:
            header.destroy()

        if len(self.props.notesDict.items()) == 0:
            self.currentNote.disable()

        for i, kv in enumerate(reversed(self.props.notesDict.items())):
            id, note = kv
            # self._notesList.rowconfigure(i+1, weight = 0)
            self._notesHeaders.append(NoteHeader(self.notesList.container))
            self._notesHeaders[-1].grid(column=0, row=i + 1, sticky="NEWS")
            self._notesHeaders[-1].update_props(
                NoteViewProps(
                    note.id,
                    note.title,
                    note.text,
                    note.creationTime,
                    note.lastChangeTime,
                )
            )

    def _render_widgets(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)

        self.newButton = Flexible(tk.Button)(self, text="New")
        self.newButton.grid(column=0, row=0, sticky="NEWS")
        self.saveButton = Flexible(tk.Button)(self, text="Save")
        self.saveButton.grid(column=1, row=0, sticky="NEWS")
        self.deleteButton = Flexible(tk.Button)(self, text="Delete")
        self.deleteButton.grid(column=2, row=0, sticky="NEWS")
        self.notesList = Scrollable(self)
        self.notesList.grid(column=0, row=1, columnspan=3, sticky="NEWS")
        self.notesList.container.columnconfigure(0, weight = 1)
        self._notesHeaders = []
        self.currentNote = CurrentNote(self)
        self.currentNote.grid(column=4, row=0, rowspan=2, sticky="NEWS")
