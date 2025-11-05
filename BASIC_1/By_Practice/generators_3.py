

    # Fibanocci series

def fib(n):
    a,b = 0,1
    while a<=n:
        yield a
        a,b = b,a+b
for x in fib(50):
    if x>30:
        break
    print(x)