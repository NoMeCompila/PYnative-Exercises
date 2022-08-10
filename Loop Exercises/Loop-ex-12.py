"""
Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
"""

n1 = 0
n2 = 1
next_num = 10
for i in range(10):
    print(n2)
    next_num = n1 + n2
    n2 = next_num

