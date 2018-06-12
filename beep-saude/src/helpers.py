from datetime import date, timedelta
from constants import DATE_FORMAT


def get_previous_dates(n):
    '''
        get previous dates including today in a list
    '''
    dates = []
    for n in range(n):
        dates.append((date.today() - timedelta(n)).strftime(DATE_FORMAT))
    return dates


def compose_redis_key(*args):
    return ":".join(args)
