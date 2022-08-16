"""
Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.


"""


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"



class Bus:


    def __init__(self, name="Fer Bus", max_speed=400, mileage=50):
        super(name, max_speed, mileage).__init__()



b1 = Bus()


print()
