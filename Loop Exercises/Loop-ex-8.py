"""
Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
50
40
30
20
10
"""

l = [10, 20, 30, 40, 50]

n = len(l) - 1
while n >= 0:
    print(l[n])
    n -= 1
