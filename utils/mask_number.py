
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
