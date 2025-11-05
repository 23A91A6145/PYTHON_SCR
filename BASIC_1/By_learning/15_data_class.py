# Data classes

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # Regular Python method should be inside the class
    def book_info(self):
        return f"{self.title} by {self.author}"

# Existing code that creates book instances
b1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224, 10.99)
b2 = Book("The Restaurant at the End of the Universe", "Douglas Adams", 256, 12.99)

# Printing out the title of book one and the author of book two
print(b1.title)
print(b2.author)

# Demonstrating the repr method
print(b1)

# Demonstrating the equality comparison
b3 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224, 10.99)
print(b1 == b3)
print(b1 == b2)

# Modifying attributes of a book
b1.title = "A Hitchhiker's Guide to the Galaxy"
b1.pages = 230

# Printing the book info
print(b1.book_info())