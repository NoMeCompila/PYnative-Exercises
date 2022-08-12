"""
Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.

Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:

200 present in a dict
"""

sample_dict = {'a': 100, 'b': 200, 'c': 300}


def is_in_dict(dict1: dict, n: int) -> None:
    l1 = list(dict1.values())
    if n in l1:
        print(f"{n} present in the dict")
    else:
        print(f"{n} not present in the dict")


is_in_dict(sample_dict, 200)
is_in_dict(sample_dict, 201)

