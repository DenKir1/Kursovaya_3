from datetime import datetime
import json


def compare_dates(date_one, date_two):
    """
    :param date_one: str date
    :param date_two: str date2
    :return: True if first > second
    """
    if date_one:
        if date_two:
            d_obj1 = datetime.strptime(date_one, '%Y-%m-%dT%H:%M:%S.%f')
            d_obj2 = datetime.strptime(date_two, '%Y-%m-%dT%H:%M:%S.%f')
            return d_obj1 > d_obj2
        return True


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


def mask_num(str_number):
    """
    :param str_number: str with 'visa 123456789'
    :return: str with  'visa 1234 45*****1234'
    """
    if not str_number:
        return
    if 'Счет' in str_number:
        return 'Счет **' + str_number[-4:]
    return str_number[:-12] + ' ' + str_number[-12:-10] + '** **** ' + str_number[-4:]


def read_file(path):
    """
    :param path: str path to json file
    :return: dict from file
    """
    if path:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        return data
    return


def sort_five(array):
    """
    :param array: list
    :return: the newest five
    """
    if array:
        a_one = array[0]
        a_two = {"date": None}
        a_three = {"date": None}
        a_four = {"date": None}
        a_five = {"date": None}
    for i in range(1, len(array)):
        if array[i]:  # find not none
            a_ = array[i]
        else:
            continue
        if exec_tr(a_):  # find EXECUTED
            if compare_dates(a_["date"], a_one["date"]):
                a_one, a_two = a_, a_one
            elif compare_dates(a_["date"], a_two["date"]):
                a_two, a_three = a_, a_two
            elif compare_dates(a_["date"], a_three["date"]):
                a_three, a_four = a_, a_three
            elif compare_dates(a_["date"], a_four["date"]):
                a_four, a_five = a_, a_four
            elif compare_dates(a_["date"], a_five["date"]):
                a_five = a_
    return a_one, a_two, a_three, a_four, a_five


def required_str(array):
    """
    :param array: dict
    :return: formated str
    """
    if array.get("from"):
        return f"""{format_time(array["date"])} {array["description"]}
{mask_num(array["from"])} -> {mask_num(array["to"])}
{array["operationAmount"]["amount"]} {array["operationAmount"]["currency"]["name"]}
"""
    return f"""{format_time(array["date"])} {array["description"]}
{mask_num(array["to"])}
{array["operationAmount"]["amount"]} {array["operationAmount"]["currency"]["name"]}
"""


def exec_tr(dict_a):
    """
    :return: True if EXECUTED
    """
    return dict_a["state"] == 'EXECUTED'
