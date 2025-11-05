
# UserDict,UserList,UserString

# UserList is a list like container that acts as a wrapper around the list objects
# simillarlly all

from collections import UserString
my_user_string = UserString("Hello, UserString!")
print(my_user_string.data)
another_user_string = UserString(" How are you?")
combined_string = my_user_string + another_user_string
print(combined_string)