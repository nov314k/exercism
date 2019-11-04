import calendar
from datetime import date

DAY_CODES = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

INDICES = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'last': -1
}


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar()
    days = [it for it in cal.itermonthdays2(year, month) if it[0] > 0]
    same_days = [day for day in days if day[1] == DAY_CODES[day_of_week]]
    teenth_days = [day for day in same_days if day[0] > 12]
    if week == 'teenth':
        return date(year, month, teenth_days[0][0])
    if week in INDICES.keys():
        if len(same_days) > INDICES[week]:
            return date(year, month, same_days[INDICES[week]][0])
        else:
            raise MeetupDayException("Nonexistent day")
