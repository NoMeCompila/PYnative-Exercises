"""
Write a Python program to get a dictionary from an object's fields.
"""

class Colors(object):
    def __init__(self):
        self.c1 = "red"
        self.c2 = "blue"
        self.c3 = "green"

    def do_nothing(self):
        pass


colores = Colors()

d1 = colores.__dict__

print(d1)