"""
Write a Python program to check a dictionary is empty or not
"""

d1 = dict()
d2 = {1: 2, 3: 3}


def is_dict_empty(d):
    return d == {}


print(is_dict_empty(d2))