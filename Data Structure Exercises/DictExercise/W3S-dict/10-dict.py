"""
Write a Python program to sum all the items in a dictionary
"""
from functools import reduce

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print("Sum all keys")

keys = 0
values = 0
key_values = 0

# con for
for i in d1:
    keys += i

for i in d1.values():
    values += i

for k, v in d1.items():
    key_values += k+v


print(f"suma de llaves =  {keys}")
print(f"suma de valores =  {values}")
print(f"suma de llaves + valores =  {key_values}")

print()
# con reduce

keys = reduce(lambda x, y: x + y, d1.keys())
print(f"suma de llaves con reduce = {keys}")

values = reduce(lambda x, y: x + y, d1.values())
print(f"suma de valores con raduce = {values}")

key_values = sum(list(reduce(lambda x, y: x + y, d1.items())))
print(f"suma de valores y llaves con reduce = {key_values}")

# con el sum

print()

keys = sum(d1.keys())
values = sum(d1.values())
key_values = sum([keys, values])

print(f"suma de llaves con sum() = {keys}")
print(f"suma de valores con sum() = {values}")
print(f"suma de llaves y valores con sum() = {key_values}")
