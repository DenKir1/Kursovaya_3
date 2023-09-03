from utils.Transaction import *


def sort_five(array):
    """
    :param array: list Transaction
    :return: newest five Transaction
    """
    if array:
        a_one = Transaction(*array[0].values())
        a_two = Transaction(None, None, '0001-01-01T10:50:58.294041', None, None)
        a_three = Transaction(None, None, '0001-01-01T10:50:58.294041', None, None)
        a_four = Transaction(None, None, '0001-01-01T10:50:58.294041', None, None)
        a_five = Transaction(None, None, '0001-01-01T10:50:58.294041', None, None)
    for i in range(1, len(array)):

        if array[i]:  # find not none
            a_ = Transaction(*array[i].values())
        else:
            continue
        if a_.exec_tr():  # find EXECUTED
            if a_.newest_than(a_one):
                a_one, a_two = a_, a_one
            elif a_.newest_than(a_two):
                a_two, a_three = a_, a_two
            elif a_.newest_than(a_three):
                a_three, a_four = a_, a_three
            elif a_.newest_than(a_four):
                a_four, a_five = a_, a_four
            elif a_.newest_than(a_five):
                a_five = a_
    return a_one, a_two, a_three, a_four, a_five
