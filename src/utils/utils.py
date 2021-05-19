# -*- coding: utf-8 -*-
"""Different utils for app functioning."""

import datetime


def getNumberOfDays(day: datetime.date) -> int:
    """Get number of days in given month."""
    dayInNextMonth = day.replace(day=28) + datetime.timedelta(days=4)
    return (dayInNextMonth - datetime.timedelta(days=dayInNextMonth.day)).day


def getFirstDayOfNextMonth(day: datetime.date) -> datetime.date:
    """Switch to next month."""
    nextMonth = day.month + 1
    nextYear = day.year

    if nextMonth > 12:
        nextYear += 1
        nextMonth = 1

    return datetime.date(nextYear, nextMonth, 1)


def getFirstDayOfPrevMonth(day: datetime.date) -> datetime.date:
    """Switch to previous month."""
    prevMonth = day.month - 1
    prevYear = day.year

    if prevMonth < 1:
        prevYear -= 1
        prevMonth = 12

    return datetime.date(prevYear, prevMonth, 1)
