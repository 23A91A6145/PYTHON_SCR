

    # Equality and comparison magic methods.

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return self.price < value.price

B1 = Book("War and Peace", "Tolstoy", 39.95)
B2 = Book("Catcher in the Rye", "Salinger", 29.95)
B3 = Book("War and Peace", "Tolstoy", 39.95)
B4 = Book("Kill Maker", "Findley", 24.95)

books = [B1, B3, B2, B4]
books.sort()
print([book.title for book in books])
