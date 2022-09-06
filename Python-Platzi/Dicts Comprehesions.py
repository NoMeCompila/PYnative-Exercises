"""
genrerar un diccionario que tenga como llave los valores en un rango de 1 a 10-0 y como valor esa llabve elevada
al cuadrado
"""

from math import sqrt

d1 = {i: i**3 for i in range(1,101) if i % 3 != 0}
print(d1)

d2 = {i:sqrt(i) for i in range(1, 1001)}

print(d2)