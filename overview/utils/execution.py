# -*- coding: utf-8 -*-
"""Utils for job execution."""
import asyncio
import threading
from typing import Coroutine


def run_in_background(cor: Coroutine) -> threading.Thread:
    """Execute async job in a background thread."""
    thread = threading.Thread(
        target=lambda l: l.run_until_complete(cor), args=(asyncio.get_event_loop(),)
    )
    thread.start()
    return thread
