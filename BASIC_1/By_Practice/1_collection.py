         # Collections

    # There are mainy 4 types of collections
    # list,tuple,set,dict

# spelizesd collections are namedtuple(),Chainmap,deque,Counter,OrderDict,defaultdict,UserDict,UserList,UserString

    # 1.NamedTuple
# It is like a regular tuple but with named fields, making data more readable and accessible

from collections import namedtuple
student= namedtuple('student',['first','last'])
student= student(first='John',last='Doe')
print(student)