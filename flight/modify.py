def addzero(str):
    if (str=='0'):
        return '00';
    elif (int(str) < 10):
        return '0' + str
    else:
        return str