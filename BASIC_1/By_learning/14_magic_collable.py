

    # Collable objects

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, Price: {self.price}"

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("The cat in the hat", "Dr. Seuss", 12.99)
b2 = Book("Green Eggs and Ham", "Dr. Seuss", 9.99)

print(b1)
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
