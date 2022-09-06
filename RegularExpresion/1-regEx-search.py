"""
Examina a través de la string buscando el primer lugar donde el pattern de la expresión regular
produce una coincidencia, y retorna un objeto match correspondiente. Retorna None si ninguna posición en la cadena
coincide con el patrón
"""

import re

txt = "Learning about regular expressions"

print(re.search("regular", txt))
# returns an object if the word is in text else returns None


def is_in_text(word: str, text: str) -> None:

    x = re.search(word, text)

    if x is not None:
        print(f"{word} is  in text")
    else:
        print(f"{word} is not in text")


txt = "Learning about regular expressions"
word1 = "Python"
word2 = "Learning"

is_in_text(word1, txt)
is_in_text(word2, txt)


