import functools

# reduce(function,sequence)

from functools import reduce
val= reduce(lambda a,b:a+b,[12,34,5,23,78,2])
print(val)