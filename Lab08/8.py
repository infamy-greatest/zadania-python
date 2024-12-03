from math import floor


def dec_to_num(num):
    if num == 1:
        return '1'
    elif num % 2 == 0:
        return str(dec_to_num(num / 2)) + '0'
    else:
        return str(dec_to_num(floor(num / 2))) + '1'


print(dec_to_num(156))
