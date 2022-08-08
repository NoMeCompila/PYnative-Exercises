"""
Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def generate_pyramid(x):
    for i in range(x+1):
        print(f"{i} " * i)


generate_pyramid(5)
