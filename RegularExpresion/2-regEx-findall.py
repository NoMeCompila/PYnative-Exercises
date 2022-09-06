"""
findall
Retorna todas las coincidencias no superpuestas de pattern en string, como una lista de strings o tuplas. El string se
escanea de izquierda a derecha y las coincidencias se retornan en el orden en que se encuentran
"""

import re

txt = "Globant is great a place to work. Globant makes me grrow"

text_find = "Globant"

lst = re.findall(text_find, txt)

# return a list with all occurrences of the searched word
print(lst)

# returns the number of occurrenes
print(len(lst))

