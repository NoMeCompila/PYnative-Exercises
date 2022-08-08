"""
Write a program to find how many times substring “Emma” appears in the given string
"""

str_x = "Emma is good developer. Emma is a writer"


def how_many(x):
    n = x.count("Emma")
    return f"Emma appeared {n} times"


print(how_many(str_x))
