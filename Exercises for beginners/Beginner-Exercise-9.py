"""
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
"""


def is_palindrome(x):

    cadena = str(x)

    lista = []
    for i in cadena:
        lista.append(i)

    reversed_list = lista[::-1]

    junto = ''.join(reversed_list)
    return junto == cadena


x = "121"
print(is_palindrome(x))

y = "122"
print(is_palindrome(y))

