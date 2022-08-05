"""
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:
remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
"""


def remove_n():
    s = input("Please enter a word: ")
    n = int(input("Please enter a digit: "))

    if len(s) < n:
        print("Invalid data, please try Again...")
        print(remove_n())
    else:
        return s[n:]


cadena = "Pynative"
x = 2

print(remove_n())
