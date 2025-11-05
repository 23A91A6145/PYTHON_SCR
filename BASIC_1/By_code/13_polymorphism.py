

    # Polymorphism

#  ability of an object to take on many forms, or more specifically, the ability
# of different objects to respond to the same method call in their own specific ways

# Mainly of 4 methods
# 1. Method Overriding
# 2. Method Overloading 
# 3. Operator Overloading
# 4. Duck Typing



# Method Overriding

# Method Overriding

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!