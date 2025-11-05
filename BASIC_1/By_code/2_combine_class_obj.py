# combining classes and objects

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof!")

class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.phone = contact

owner1 = Owner("Alice", "123 Main St", "555-1234")
dog1 = Dog("Buddy", "Golden Retriever", owner1)  # Removed extra parenthesis
dog1.bark()
print(dog1.name)

owner2 = Owner("Bob", "456 Elm St", "555-5678")
dog2 = Dog("Max", "Beagle", owner2)
print(dog2.owner.name)
print(dog2.owner.address)