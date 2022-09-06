"""
Write a Python script to check whether a given key already exists in a dictionary.
"""


def is_in_dict(d, k):
    return k in (d.keys())


d1 = {1: 2, 3: 2, 5: 5}
k1 = 3

print(is_in_dict(d1, k1))