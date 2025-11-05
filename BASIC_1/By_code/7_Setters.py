from datetime import datetime


class User2:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self._email = email
        self.isAdmin = isAdmin

    def getEmail(self):
        if self.isAdmin:
            print(f"Email accessed at {datetime.now()}")
            return self._email
        return None 
    
    def setEmail(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail


user1 = User2("dantheman", "dan@gmail.com", True)
print(user1._email)  

user1.setEmail("dan@outlook.com")
print(user1.getEmail())