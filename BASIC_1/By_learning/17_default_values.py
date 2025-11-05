

    # Default values in data classes

import dataclasses
from dataclasses import dataclass, field
import random

@dataclass
class Book:
    title: str = "Default Title"
    author: str = "Default Author"
    pages: int = 0
    price: float = field(default_factory=lambda: random.uniform(20, 40))

# Create a function to generate a random price between 20 and 40
def price_funk():
    return random.uniform(20, 40)

# Create a couple of books with non-default data except for the price
B2 = Book("title2", "author2")
B3 = Book("title3", "author3")

# Print out B2 and B3
print(B2)
print(B3)
