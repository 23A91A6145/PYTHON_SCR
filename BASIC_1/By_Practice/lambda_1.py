

    # Lambda ananomus functions
# lambda arguments: expression

x=lambda a: a*a
# x(2)
print(x(2))

# lambda with user defined functions
def new(x):
    return (lambda y: x+y)
t=new(3)
print(new(2))
