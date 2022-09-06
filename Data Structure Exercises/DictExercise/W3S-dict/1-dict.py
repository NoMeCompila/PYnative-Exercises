"""
Write a Python program to sort (ascending and descending) a dictionary by value.
"""
import operator
from pprint import pprint as pp

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print()
print("\t===Sorted and lambda expression===")
print()
print("By Value")
print(f"original list: {d}")

sorted_dict = dict(sorted(d.items(), key=lambda x:x[1]))
print("Sorted list:", end=" ")
pp(sorted_dict)
print()
print("By Key")
print(dict(sorted(d.items(), key=lambda x:x[0])))

print()
print("\t===Reversed order and lambda expression===")
print()
print("By Value")
reversed_dict = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
print(reversed_dict)
print()
print("By Key")
reversed_dict = dict(sorted(d.items(), key=lambda x:x[0], reverse=True))
print(reversed_dict)
print()

print("\t===Sorted with operator library===")
print()
print("By Value")
d1 = {"a": 2, "g": 4, "x": 3, "l": 1, "p": 0}
sorted_d = dict(sorted(d1.items(), key=operator.itemgetter(1)))
print(sorted_d)
print()
print("By Key")
sorted_d = dict(sorted(d1.items(), key=operator.itemgetter(0)))
print(sorted_d)
print()
