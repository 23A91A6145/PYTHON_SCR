

    # Attribute private(protected) in Python

#  It is acessed by using  underscore(_) before the attribute name.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.strip().lower()

user1 = User("dantheman", " Dan@gmail.com ", "123")
print(user1._email)
print(user1.clean_email())


# protected attribute can still be accessed from outside the class.
# It is represented by __ underscore before the attribute name.

# Protected methods are indicated by prefixing their names with a single underscore (_).
# Private methods are indicated by prefixing their names with a double underscore (__).