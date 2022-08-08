"""
Write a program to accept two numbers from the user and calculate multiplication
"""


def product_nums():
    try:
        x = int(input("enter a digit please: "))
        y = int(input("enter another digit please: "))
        print(f"{x} * {y} = {x * y}")
    except ValueError:
        print("invalid numbers try again")
        product_nums()


product_nums()



