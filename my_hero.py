#A simple program demonstrating the use of classes and objects in python
# #creating a class called Superhero


class Superhero:

    def __init__(self, name, country, tribe):

        self.name = name
        self.country = country
        self.tribe = tribe

    def __str__(self):
        return f"{self.name} is a superhero from {self.country} and belongs to the {self.tribe} tribe."
    
class Children(Superhero):

    def __init__(self, name, country, tribe,child_name, child_age):
        super().__init__(name, country, tribe)
    
        self.child_name = child_name
        self.child_age = child_age  
    def __str__(self):
        return f"{self.child_name} is the child of {self.name} and is {self.child_age} years old."
    
my_superhero = Superhero("Wangari Maathai", "Kenya", "Kikuyu")
my_family = Children("Wangari Maathai", "Kenya", "Kikuyu", "Wanjiru", 53)

print(my_superhero)
print(my_family)