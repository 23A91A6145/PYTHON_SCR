# Using instance attributes

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'hidden'  # Double underscore makes this a "private" attribute

    def getprice(self):
        # Single underscore indicates a "protected" member by convention
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount

b1 = Book('python oops', 'abc', 200, 250)

b1.setdiscount(0.12)
print(b1.getprice())      # Prints discounted price
print(b1.price)           # Prints original price

# Properties with double underscore are name-mangled (not truly hidden)
print(b1._Book__secret)   # Accessing the "private" attribute