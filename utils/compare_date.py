from datetime import datetime


def compare_dates(date_one, date_two):
    """
    :param date_one: str date
    :param date_two: str date2
    :return: True if first > second
    """
    d_obj1 = datetime.strptime(date_one, '%Y-%m-%dT%H:%M:%S.%f')
    d_obj2 = datetime.strptime(date_two, '%Y-%m-%dT%H:%M:%S.%f')
    return d_obj1 > d_obj2
