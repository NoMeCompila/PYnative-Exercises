import json


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicle_decoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])


vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }', object_hook=vehicle_decoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)


class Person:
    def __init__(self, name, last_name, dni, mail):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.mail = mail


def person_decorator(per):
    return Person(per['name'], per['last_name'], per['dni'], per['mail'])


p1 = json.loads('{"name": "Fernando", "last_name": "Caballero", "dni": "40982473", "mail": "cabafer1@globant.com"}',
                object_hook=person_decorator)

print("Type of decoded object from JSON Data")
print(type(p1))
print("Person Details")
print(p1.name, p1.last_name)
