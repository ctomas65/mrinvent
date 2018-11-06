def xstr(value):
    """
    Return a safe string value
    :param value: the original value
    :return: the safe string value
    """
    return str(value) if str is not None \
        else 'None'
