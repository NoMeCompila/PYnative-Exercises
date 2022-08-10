"""
A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
"""

num1 = 0
num2 = 1

for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res

