
    # 3.Chainmap
# It is a dictionary like class for creating a single view of multiple mappings

from collections import ChainMap

a= {1:'edureka',2:'python'}
b= {3:'ML',4:'AI'}

c= ChainMap(a, b)
print(c)