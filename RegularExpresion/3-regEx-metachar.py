"""
escape(pattern)
Caracteres de escape especiales en pattern (» patrón»). Esto es útil si quieres hacer coincidir una
cadena literal arbitraria que puede tener metacaracteres de expresión regular en ella
"""
import re

names = ["Fernando Caballero", "Jeremias Barrios", "Leandro Caballero", "Susana Acosta", "Susana Cabalero"]

# retorna todos los que empiecen por esa letra o cadena
sus = []

for i in names:
    if re.findall("^Susana", i):
        sus.append(i)

print(sus)


# retorna todos los que terminen por esa letra o cadena
cabas = []


for i in names:
    if re.findall("Caballero$", i):
        cabas.append(i)

print(cabas)


# retorna todos los contengan  los caracteres indicados o dentro de un rango

words = [
    'nenes',
    'nenas',
    'hombre',
    'mujer'
]

nen = []
for i in words:
    if re.findall("nen[ea]s", i):
        nen.append(i)

print(nen)




words = [
    'nenes',
    'nenas',
    'hombre',
    'mujer',
    'felicidad',
    'Jaff'
]

finales = []

for i in words:
    if re.findall("[d-f]$", i):
        finales.append(i)

print(finales)