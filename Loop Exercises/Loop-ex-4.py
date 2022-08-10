"""
Write a program to print multiplication table of a given number
For example, num = 2 so the output should be
2
4
6
8
10
12
14
16
18
20
"""


def prod_table():
    try:
        n = int(input("enter a integer digit: "))
        for i in range(0, 11):
            print(i*n)
    except ValueError:
        print("Invalid digit, try again...")
        prod_table()


prod_table()