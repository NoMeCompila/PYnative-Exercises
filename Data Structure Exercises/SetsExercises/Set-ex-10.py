"""
Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)

Expected output:
True
"""
t1 = (45, 45, 45, 45)

x = True
for i in range(1,4):
    if t1[i] != t1[i-1]:
        x = False

print(x)