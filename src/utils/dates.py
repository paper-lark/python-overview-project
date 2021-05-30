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


def translateMonth(dt_string: str) -> str:
    """Get datetime str with localized month."""
    monthTranslated = {
        "Jan": _("Jan"),
        "Feb": _("Feb"),
        "Mar": _("Mar"),
        "Apr": _("Apr"),
        "May": _("May"),
        "Jun": _("Jun"),
        "Jul": _("Jul"),
        "Aug": _("Aug"),
        "Sep": _("Sep"),
        "Oct": _("Oct"),
        "Nov": _("Nov"),
        "Dec": _("Dec"),
    }[dt_string.split(" ")[1]]

    res = " ".join([dt_string.split(" ")[0], monthTranslated])
    if len(dt_string.split(" ")) > 2:
        res = " ".join([res, *(dt_string.split(" ")[2:])])

    return res


def getDayMonthYear(day: datetime.date) -> str:
    """Format date."""
    return day.strftime("%d %b %Y")


def getMonthYear(day: datetime.date) -> str:
    """Format date to get month and year only."""
    return day.strftime("%Y %b")


def getDatetimeFromDay(day_string: str) -> datetime.date:
    """Format date string."""
    return datetime.datetime.strptime(day_string, "%d %b %Y").date()
