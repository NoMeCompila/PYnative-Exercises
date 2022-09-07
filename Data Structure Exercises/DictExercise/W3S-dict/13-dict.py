"""
Write a Python program to map two lists into a dictionary.

must returns:
d1 = {1: 1, 2: 4, 3: 9}
"""

l1 = [1, 2, 3]

l2 = [1, 4, 9]

d1 = dict(zip(l1, l2))

print(d1)
