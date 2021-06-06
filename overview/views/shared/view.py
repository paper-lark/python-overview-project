# -*- coding: utf-8 -*-
"""Abstract view."""
import tkinter as tk
from abc import abstractmethod
from typing import Generic, Optional, TypeVar

from overview.views.shared.flexible import Flexible

Props = TypeVar("Props")


class View(Flexible(tk.Frame), Generic[Props]):
    """Abstract view to be used for MVC."""

    def __init__(self, *args, **kwargs):
        """Construct abstract view."""
        super().__init__(*args, **kwargs)
        self.props: Optional[Props] = None
        self._render_widgets()

    def update_props(self, props: Props):
        """Update view props."""
        self.props = props
        self._update()

    @abstractmethod
    def _update(self):
        """Update view props."""
        pass

    @abstractmethod
    def _render_widgets(self):
        """Render widgets without state."""
        pass
