
    # 4.Counter
# It is a dictionary subclass for counting hashable objects

from collections import Counter

a= [1,3,2,1,2,5,6,7,4,6,9]
c= Counter(a)
print(c)

print(list(c.elements()))

print(c.most_common())

sub= {2:1,6:2}
print(c.subtract(sub))
print(c)
print(c.most_common())
