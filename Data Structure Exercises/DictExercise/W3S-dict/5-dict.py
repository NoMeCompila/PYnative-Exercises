"""
Write a Python program to iterate over dictionaries using for loops.
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("imprimir llaves con for")
for i in d:
    print(i, end=" ")

print("\nimprimir valores con for")
for i in d.values():
    print(i, end=" ")