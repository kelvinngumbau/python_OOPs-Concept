#A simple program to demonstrate how polymorphism works in python

#creating a class called Vehicles

class Vehicles:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        return f"my {self.name} is {self.model} and I am driving."

class plane:

    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is flying."

my_vehicle = Vehicles("car", "BMW")
my_plane = plane("Boeing")

print(my_vehicle.move())
print(my_plane.move())