"""
calcular el factorial de un numero
"""

def factorial(x):
    result = 1
    n = x

    while(n > 1):
        result *= n
        n -= 1

    return result

num = 0

print(factorial(num))

