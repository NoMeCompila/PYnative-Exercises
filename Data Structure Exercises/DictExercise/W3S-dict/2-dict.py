"""
Write a Python script to add a key to a dictionary.
"""
dic1 = {1: 10, 2: 20}
print(f"original: {dic1}")
dic1.update({5: 5})

print(f"after adding: {dic1}")

# Otra forma
dic1[7] = 70

print(f"with bracket notation: {dic1}")
