#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    c = (a & b)
    msg = ''.join(c)
    return msg