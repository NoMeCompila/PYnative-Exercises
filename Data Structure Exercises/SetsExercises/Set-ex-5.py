"""
Swap two tuples in Python

Given:
tuple1 = (11, 22)
tuple2 = (99, 88)

Expected output:
tuple1: (99, 88)
tuple2: (11, 22)
"""


t1 = (11, 22)
t2 = (99, 88)


t1, t2 = t2, t1

print(t1)
print(t2)
