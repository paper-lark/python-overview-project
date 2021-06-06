#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Application setup module."""
import gettext
import tkinter as tk

from overview.controllers.app import AppController


def run():
    """Run application."""
    gettext.install("messages", localedir="locale")
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = AppController(root=root)
    app.start()
