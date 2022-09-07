"""
Write a Python program to remove a key from a dictionary
"""

d1 = {1: 1, 2: 4, 3: 9}
print(f"original: {d1}")

del d1[1]
print(f"despues de remover con \"del\": {d1}")

d1.pop(2)
print(f"despeus de remover con pop(key): {d1}")

print()
print("reseteo de diccionario")
d1 = {1: 1, 2: 4, 3: 9}

# devuelve un KeyError
# del d1[5]
# print(d1)# esto dara error
# en cambio con pop() si no se encuentra la llave en el diccionario entonces retorna None
# d1.pop(5)

