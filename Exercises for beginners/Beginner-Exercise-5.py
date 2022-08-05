"""
Write a function to return True if the first and last number of a given list is same. If numbers are different
then return False.
"""


def first_last(cad: list) -> bool:
    return True if cad[0] == cad[-1] else False


l = [0, 1, 2, 0, 1]

print(first_last(l))