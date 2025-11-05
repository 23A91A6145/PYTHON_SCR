# Multiple Inheritance

class A:
    def __init__(self):
        self.prop_one = "prop one"
        self.name = "class A"

class B:
    def __init__(self):
        self.prop_two = "prop two"
        self.name = "class B"

class C(A, B):  # Or class C(B, A): to change the order
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def show_props(self):
        print(self.prop_one)
        print(self.prop_two)
        print(self.name)

c = C()
c.show_props()
print(C.__mro__)