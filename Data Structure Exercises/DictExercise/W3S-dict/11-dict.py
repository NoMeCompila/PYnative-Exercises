"""
Write a Python program to multiply all the items in a dictionary
"""
from functools import reduce

d1 = {1: 1, 2: 4, 3: 9}


x = 1
for i in d1:
    x *= i

print(f"producto de llaves con for = {x}")

x = reduce(lambda i, j: i * j, d1)

print(f"producto de llaves con reduce() = {x}")


print()
x = 1
for i in d1.values():
    x *= i

print(f"producto de valores con for = {x}")

x = reduce(lambda i, j: i * j, d1.values())

print(f"producto de valores con reduce() = {x}")

print()

x = 1
for i, j in d1.items():
    x *= i * j

print(f"producto de llaves y valores con for = {x}")

x = reduce(lambda i, j: i * j, d1.values())
y = reduce(lambda i, j: i * j, d1.keys())

print(f"producto de llaves y valores con reduce() = {x * y}")
