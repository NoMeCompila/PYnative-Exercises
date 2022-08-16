"""
Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""


class Auto():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


a1 = Auto(240, 1400)
print(a1.max_speed)
print(a1.mileage)


