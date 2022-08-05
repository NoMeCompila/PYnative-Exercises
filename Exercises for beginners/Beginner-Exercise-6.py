"""
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""


l1 = [1, 2, 5, 10, 4, 20, 55, 50, 3, 100]

div_5 = list(filter(lambda x: x % 5 == 0, l1))

print(div_5)