

    # Generators are created using def keyword and use yeild instead of return

def new(dict):
    for x, y in dict.items():
        yield x, y

a = {1: 'hi', 2: 'welcome'}
b = new(a)
print(next(b))
# we need to use next keyword for use functions
print(next(b))
