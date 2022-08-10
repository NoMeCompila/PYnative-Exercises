"""
Write a program to create function calculation() such that it can accept two variables and calculate addition and
subtraction. Also, it must return both addition and subtraction in a single return call.
"""


def get_sum_sub(x: int, y: int) -> tuple:
    return x+y, x-y


print(get_sum_sub(5, 3))

