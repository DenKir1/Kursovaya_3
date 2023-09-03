from compare_date import compare_dates
from date_from import format_time
from mask_number import mask_num


class Transaction:
    def __init__(self, id_, state_, date_, operation_, description_, from_=None, to_=None):
        self.id_ = id_
        self.state_ = state_
        self.date_ = date_
        self.operation_ = operation_
        self.description_ = description_
        self.from_ = from_
        self.to_ = to_

    def __repr__(self):
        if self.to_:
            return f"""{format_time(self.date_)} {self.description_}
{mask_num(self.from_)} -> {mask_num(self.to_)}
{self.operation_["amount"]} {self.operation_["currency"]["name"]}
"""
        return f"""{format_time(self.date_)} {self.description_}
{mask_num(self.from_)}
{self.operation_["amount"]} {self.operation_["currency"]["name"]}
"""

    def newest_than(self, other):
        """
        :param other: b - object class Transaction
        :return: true if a > b
        """
        a = self.date_
        b = other.date_
        return compare_dates(a, b)

    def exec_tr(self):
        """
        :return: True if EXECUTED
        """
        return self.state_ == 'EXECUTED'
