"""
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""


l1 = [1, 2, 5, 10, 4, 20, 55, 50, 3, 100]

l2 = [1, 2, 3, 4, 5]

div_5 = list(filter(lambda x: x % 5 == 0, l1))

only_5 = list(filter(lambda x: x % 5 == 0, l2))

print(only_5)
print(div_5)