# checking instance of a class

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):  # Fixed typo: should be __init__ not _init__
        self.name = name

b1 = Book('python oops')
b2 = Book('java oops')
n1 = Newspaper('the times of india')
n2 = Newspaper('the hindu')

print(type(b1))                  # <class '__main__.Book'>
print(type(n1))                  # <class '__main__.Newspaper'>

# comparing two types

print(type(b1) == type(b2))      # True
print(type(b1) == type(n1))      # False
    
# using isinstance() function

print(isinstance(b1, Book))      # True
print(isinstance(b1, Newspaper)) # False