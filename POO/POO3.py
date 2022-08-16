"""
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Expected Output:

Vehicle Name: School Volvo Speed: 180 Mileage: 12
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __int__(self, name, max_speed, mileage):
        super().__int__(name, max_speed, mileage)



b1=Bus("asdasd", 500, 600)

print(b1.name)
