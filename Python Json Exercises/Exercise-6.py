import json
from json import JSONEncoder


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class Encoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=Encoder)
print(vehicleJson)


class Users:
    def __init__(self, page, per_page, total, total_pages, data):
        self.page = page
        self.per_page = per_page
        self.total = total
        self.total_pages = total_pages
        self.data= data


users = Users(2,6,12,2,[{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"}])


print("Encode Users Object into JSON")
usersJson = json.dumps(users, indent=4, cls=Encoder)
print(usersJson)