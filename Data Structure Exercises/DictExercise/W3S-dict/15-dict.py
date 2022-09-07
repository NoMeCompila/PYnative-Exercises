"""
Write a Python program to get the maximum and minimum value in a dictionary
"""

d1 = {"c": 4, "a": 1, "d": 2}

max_k = max(d1.values())
max_v = max(d1.keys())

max_kv = max(d1.items(), key=lambda x: x[1])
print(max_kv)
print(f"{max_kv[0]} {max_kv[1]}")

max_kv = min(d1.items(), key=lambda x: x[1])
print(max_kv)
print(f"{max_kv[0]} {max_kv[1]}")

sor = dict(sorted(d1.items(), key=lambda x:x[1]))
print(sor)
sor1 = dict(sorted(d1.items(), key=lambda x:x[0]))
print(sor1)
