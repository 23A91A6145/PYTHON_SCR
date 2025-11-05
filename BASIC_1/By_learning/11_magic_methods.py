

    # String representation of objects

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    def __repr__(self):
        return f"Title = {self.title}, Author = {self.author}, Price = {self.price}"


B1 = Book("Gone with the Wind", "Margaret Mitchell", 12.99)
B2 = Book("The Hobbit", "J.R.R. Tolkien", 9.99)

print(B1)
print(B2)

print(str(B1))
print(repr(B2))
