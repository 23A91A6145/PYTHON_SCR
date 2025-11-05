

    # Interfaces

from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def to_JSON(self):
        pass

class circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def to_JSON(self):
        return f"'circle' : {str(self.calcArea())}"

c = circle(10)
print(c.calcArea())
print(c.to_JSON())
