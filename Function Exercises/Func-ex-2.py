"""
Write a program to create function func1() to accept a variable length of arguments and print their value.
"""


def multiple_args(*args):
    for i in args:
        print(i)


multiple_args(12,3,4,"a")

