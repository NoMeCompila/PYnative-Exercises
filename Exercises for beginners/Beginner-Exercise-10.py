"""
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers
from the first list and even numbers from the second list.
"""

l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]


def concat_odd_even(la, lb):
    odd = list(filter(lambda x: x % 2 != 0, la))
    even = list(filter(lambda x: x % 2 == 0, lb))

    l3 = odd + even

    return l3


print(concat_odd_even(l1, l2))

