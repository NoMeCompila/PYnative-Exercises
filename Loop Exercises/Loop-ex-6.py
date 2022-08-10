"""
Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.
"""


def num_counter(n):
    counter = 0
    x = n
    while n != 0:
        counter += 1
        n = n // 10
    print(f"number {x} has: {counter} digits")


n = 1234

num_counter(n)