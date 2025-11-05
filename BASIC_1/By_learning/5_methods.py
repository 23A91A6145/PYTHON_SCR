

class Book:
    # Class-level attribute
    BOOK_TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self, title, book_type):
        if not book_type in Book.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type")
        self.title = title
        self.book_type = book_type
    # --
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    __booklist = None

    @staticmethod
    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

B1 = Book("title one", "hardcover")
B2 = Book("comic", "paperback") #Corrected book type

books = Book.get_booklist()
books.append(B1)
books.append(B2)
print(books)
print(Book.get_book_types())