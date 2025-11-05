# Duck Typing

class Car:
    def move(self):
        return "Driving"

class Boat:
    def move(self):
        return "Sailing"

def transport(vehicle):
    print(vehicle.move())

car = Car()
boat = Boat()
transport(car)   # Output: Driving
transport(boat)  # Output: Sailing