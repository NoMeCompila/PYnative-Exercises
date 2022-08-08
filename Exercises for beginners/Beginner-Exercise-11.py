"""
Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""

x = 7536

l1 = []

for i in str(x):
    l1.append(i)

l2 = list(reversed(l1))

for i in l2:
    print(i, end=" ")
