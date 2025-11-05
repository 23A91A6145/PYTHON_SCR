
    # Inheritence
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Book(Publication):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

# Sample objects
book1 = Book("The Hound of the Baskervilles", 29.99, "Sir Arthur Conan Doyle", 336)
newspaper1 = Newspaper("The New York Times", 6.00, "Daily", "The New York Times Company")
magazine1 = Magazine("Scientific American", 6.99, "Monthly", "Springer Nature")

# Accessing data
print(book1.author)
print(newspaper1.publisher)
print(book1.price, newspaper1.price, magazine1.price)

