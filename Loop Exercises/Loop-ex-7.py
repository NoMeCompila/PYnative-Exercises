"""
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

x = 5
y = 5
for i in range(0, x+1):
    for j in range(y-i, 0, -1):
        print(j, end=' ')
    print()
