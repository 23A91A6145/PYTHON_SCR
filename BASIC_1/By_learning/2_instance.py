

        # Instances 

class Book:
     
    #  init function is called when object is created
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages=pages
        self.price=price

    # creating instance methods

    def getprice(self):
        return self.price
    
# creating some book instances

b1=Book('python oops','abc',200,250)
b2=Book('java oops','xyz',300,350)

print(b1.getprice())