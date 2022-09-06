"""
obtener el maximo de una lista de diccionarios
lista = [{‘key’:20}, {‘key’:35}, {‘key’: 44}]
"""

lista = [{'key': 20}, {'key': 35}, {'key': 44}]

l = []

for i in lista:
    l.append(i.get('key'))

print(max(l))
