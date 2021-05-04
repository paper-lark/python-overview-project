#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main module of application."""

import tkinter as tk

from controllers.app.app import AppController


def main():
    """Application entry point."""
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = AppController(parent=root)
    app.mainloop()


if __name__ == "__main__":
    main()
