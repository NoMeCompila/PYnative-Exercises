"""
Create a function in Python
Write a program to create a function that takes two arguments, name and age, and print their value.
"""


def print_personal_data(name: str, age: int) -> None:
    print(f"your name is: {name}")
    print(f"you have {age} years old")


my_name = "Fernando"
my_age = 24

print_personal_data(my_name, my_age)