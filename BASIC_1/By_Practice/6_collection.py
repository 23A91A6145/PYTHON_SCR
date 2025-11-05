from collections import defaultdict

    # 6. defaultdict
# dictionary subclas calls factory fun to supply missing values

d=defaultdict(int)
d['a']=1
d['b']=2
d['c']=1
d['d']=4

print(d)