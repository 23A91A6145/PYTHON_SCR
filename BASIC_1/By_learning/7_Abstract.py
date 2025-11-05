

    # Abstract Classes

from abc import ABC, abstractmethod

class GraphicShape(ABC):
    @abstractmethod
    def calc_area(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * self.radius * self.radius

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calc_area(self):
        return self.side * self.side

# This line will now cause an error:
# shape = GraphicShape()

circle = Circle(5)
square = Square(4)

print(f"Circle area: {circle.calc_area()}")
print(f"Square area: {square.calc_area()}")