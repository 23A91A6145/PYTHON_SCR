

    # post initialization

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

    def __post_init__(self):
        self.description = f"{self.title} by {self.author} ({self.pages} pages)"

b1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
b2 = Book("Pride and Prejudice", "Jane Austen", 432)

print(b1.description)
print(b2.description)
