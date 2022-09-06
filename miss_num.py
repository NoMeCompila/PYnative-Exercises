

l = [1, 2, 3, 4, 5, 6, 8]

miss = 0

for i in range(len(l)):
    if l[i] != i:
        miss = i+1

print(miss)