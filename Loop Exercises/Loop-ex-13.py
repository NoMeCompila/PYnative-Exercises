"""
Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
"""


def facts(n):
    x = 1
    while n != 0:
        x *= n
        n -= 1
    return x


n = 5
print(facts(n))

