

    # Acessing object data

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def sayHiToUser(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ;)"
        )


user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@gmail.com", "abc")
user1.sayHiToUser(user2)
