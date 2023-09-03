from datetime import datetime


def format_time(str_date):
    """
    :param str_date: str data with '%Y-%m-%dT%H:%M:%S.%f'
    :return: str with '%d.%m.%Y'
    """
    if str_date:
        d_obj = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
        date_true = d_obj.strftime('%d.%m.%Y')
        return date_true
    return

