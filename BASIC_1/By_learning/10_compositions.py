    

    # Compositions

class Author:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        result = 0
        for chapter in self.chapters:
            result += chapter.page_count
        return result

# Example Usage:
author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 12.99, author)

b1.add_chapter(Chapter("Chapter 1", 20))
b1.add_chapter(Chapter("Chapter 2", 30))
b1.add_chapter(Chapter("Chapter 3", 25))

print(b1.author)
print(b1.get_book_page_count())
