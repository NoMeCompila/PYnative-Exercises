"""
 Write a Python program to sort a given dictionary by key.
"""
# ordenar por llave
d1 = {"c": 4, "a": 1, "d": 2}
l1 = sorted(d1)
d2 = dict()
for i in l1:
    d2[i] = d1[i]
print(d2)


# ordenar por valor
d1 = {"c": 4, "a": 1, "d": 2}
sorted_dict = dict(sorted(d1.items(), key=lambda x: x[1]))
print(sorted_dict)

# ordenar por llave

sorted_keys = dict(sorted(d1.items(), key=lambda x: x[0]))

print(sorted_keys)

