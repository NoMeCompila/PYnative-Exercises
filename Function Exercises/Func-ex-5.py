
"""
Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
"""


def add_nums(x, y):
    return x + y


def add_5(x):
    return x + 5


def enter_nums():
    x = int(input("Enter a digit: "))
    y = int(input("Enter a digit: "))
    return add_5(add_nums(x, y))


print(enter_nums())

