"""
Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.

Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:

[1, 4, 9, 16, 25, 36, 49]
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
squares = list(map(lambda x: x*x, numbers))
print(squares)
