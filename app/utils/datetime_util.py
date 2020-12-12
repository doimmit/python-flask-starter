from datetime import datetime, time

date_format = '%m%d'
time_format = '%H%M'


def current_date():
    return datetime.now().strftime(date_format)


def current_time():
    return datetime.now().strftime(f'{date_format}_{time_format}')


def get_date_str(date):
    return date.strftime(date_format)


def get_date_by_str(date_str):
    return datetime.strptime(date_str, date_format)


def get_date_min_time(date_str):
    return datetime.combine(get_date_by_str(date_str), time.min)


def get_date_max_time(date_str):
    return datetime.combine(get_date_by_str(date_str), time.max)
