"""
determinar si una lalabnra es palindromo
generar una lista con los numeros impartes usando lambda functions
"""
from functools import reduce

palindromo = lambda str1: str1 == str1[::-1]

print(palindromo('hola'))
print(palindromo('ana'))
print(palindromo('isi'))
print(palindromo('Fernmando'))

l1 = [1, 2, 3, 4, 5, 6, 7]

odd = list(filter(lambda x: x % 2 != 0, l1))
print(odd)

squares = list(map(lambda x: x**2, l1))
print(squares)

all_multi = reduce(lambda x, y: x * y, l1)
print(all_multi)
