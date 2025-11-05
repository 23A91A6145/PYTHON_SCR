

    # Attribute acess magic methods

class Book:
    def __init__(self, title, author, price, discount):
        self.title = title
        self.author = author
        self.price = price
        self.discount = discount

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            discount = super().__getattribute__('discount')
            return p - (p * discount)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError("The price attribute must be a float")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        return name + " is not here"

# Example Usage
B1 = Book("Warren Peace", "A. Nonymous", 38.95, 0.10)
B1.price = float(42)
print(B1)
print(B1.randomProp)
