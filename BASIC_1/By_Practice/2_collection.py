
    # 2. deque

# It is the optimized list for quicker append and pop operations from both sides of the container
from collections import deque
a= ['e','d','u','r','e','k','a']
d= deque(a)
d.appendleft('python')
print(d)
d.popleft()
print(d)