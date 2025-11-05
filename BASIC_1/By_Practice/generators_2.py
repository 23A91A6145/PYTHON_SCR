

    # Generators in loops

f= range(6)
print('List comp',end=':')
q=[x+2 for x in f]
print(q)
print('gen exp', end=':')
r=[x+3 for x in f]
print(r)