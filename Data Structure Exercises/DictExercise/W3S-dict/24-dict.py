"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
"""

from collections import Counter
from pprint import pprint as pp

str1 = "w3resource"

d = dict(Counter(str1))

pp(d)



