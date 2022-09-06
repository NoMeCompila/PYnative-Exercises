"""
re.search(pattern, string, flags=0)
Examina a través de la string («cadena») buscando el primer lugar donde el pattern («patrón») de la expresión regular
produce una coincidencia, y retorna un objeto match correspondiente. Retorna None si ninguna posición en la cadena
coincide con el patrón; notar que esto es diferente a encontrar una coincidencia de longitud cero
en algún punto de la cadena.
"""

"""
\w
Para los patrones de Unicode (str):
Coincide con los caracteres de palabras de Unicode; esto incluye la mayoría de los caracteres que pueden formar parte 
de una palabra en cualquier idioma, así como los números y el guión bajo. Si se usa el indicador ASCII, sólo coincide con [a-zA-Z0-9_].
"""

import re
from pprint import pprint as pp

words = "Lorem. ipsum! dolor sit amet, -11 consectetur adipiscing elit, " \
        "sed do eiusmod tempor incididunt ut labore et dolore " \
        "magna aliqua. Et tortor consequat id porta nibh venenatis. Lorem mollis aliquam ut porttitor leo a diam. " \
        "Habitant morbi tristique senectus et netus et malesuada fames ac. Scelerisque viverra mauris in aliquam sem " \
        "fringilla ut morbi. Ipsum suspendisse 12 ultrices gravida dictum fusce. Vivamus arcu 14.5 felis bibendum ut. Erat velit " \
        "scelerisque in dictum non consectetur a erat. Tincidunt ornare massa eget egestas purus viverra accumsan in. Phasellus " \
        "vestibulum lorem 66.66 sed risus ultricies tristique nulla. Tincidunt augue interdum velit euismod. Non consectetur " \
        "a erat nam at -77 lectus. Diam ut venenatis tellus in. Consectetur libero -1 id faucibus nisl. Amet facilisis magna " \
        "etiam tempor orci eu lobortis 13 elementum nibh. Cras semper auctor neque vitae tempus quam. Vitae tortor " \
        "condimentum lacinia quis vel eros donec ac. Aliquam ut porttitor leo a diam sollicitudin tempor."

splited = re.findall(r"\w+", words)
all_nums = re.findall(r'-?\d+\.?\d*', words)
#all_nums = re.findall("\d+", words)
#[0-9]\.?[0-9]?
pp(all_nums)

from collections import Counter

cunters = dict(Counter(splited))

#pp(cunters)

# transform all nums in float

floats = list(map(lambda x: float(x), all_nums))

print(floats)