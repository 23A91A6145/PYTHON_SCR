


    # Object 

# Everything, you create in Python is an object. like  strings, lists, and even functions. 

name = "Danny"
age = 29
print(name)
print(age)
print(type(name))

    # class

# Classes are the blueprints for objects, meaning they describe what an object should look like.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
    def get_age(self):
        return self.age
    
dog1=Dog("Buddy", 3)
dog1.bark()
print(dog1.name)
print(dog1.get_age())
