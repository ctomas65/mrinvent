# coding: utf-8


def xstr(value):
    """
    Return a safe string value
    :param value: the original value
    :return: the safe string value
    """
    return str(value).encode('utf-8').decode('utf-8') if str is not None \
        else 'None'
