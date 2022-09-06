"""
intentando crear una app para obtener la duracion total de una playlist de youtube
"""
import re
# Primero obtengo todas las duraciones de una paylist utilizando sus expaths
# xpath para obtener las duraciones de los videos de una playlist
# $x('(//ytd-playlist-panel-renderer//div[@id="items"]//ytd-thumbnail-overlay-time-status-renderer//span)/text()').
# map(x => x.wholeText)
from pprint import pprint as pp

# genero una lista con las duraciones
cs_course_classes_duration = [
    '\n  1:08:40\n', '\n  1:18:04\n', '\n  1:01:41\n', '\n  1:13:41\n',
    '\n  56:45\n',   '\n  1:04:05\n', '\n  41:08\n',   '\n  53:30\n',
    '\n  57:23\n',   '\n  27:58\n',   '\n  30:48\n',   '\n  28:32\n',
    '\n  54:39\n',   '\n  1:01:30\n', '\n  1:03:34\n', '\n  45:30\n',
    '\n  57:37\n',   '\n  50:21\n',   '\n  52:53\n',   '\n  33:07\n',
    '\n  54:33\n',   '\n  22:31\n',   '\n  33:18\n']

print("original list:")
pp(cs_course_classes_duration)

# con ayuda de un map y la funcion strip quito los espacios en blanco de cada elemento de la lista

#only_classes_duration = []
#for i in cs_course_classes_duration:
#    only_classes_duration.append(i.strip())
print()
only_classes_duration = list(map(lambda x: x.strip(), cs_course_classes_duration))
print("List after transformation: ")
pp(only_classes_duration)







