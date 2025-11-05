# Encapsulation

# It ensures that an object's data is protected and can only be manipulated in a 
# controlled and predictable manner, leading to more robust, maintainable, and secure code.

class BankAccount2:
    def __init__(self):
        self._balance = 0.0

    # "Getter" property provides controlled access to _balance attr.
    @property
    def balance(self):
        return self._balance

    # If we don't provide a setter property, then _balance cannot be set directly outside of the class, providing safety against the balance being set to an invalid amount. To modify _balance, the provided deposit and withdraw api methods must be used.
    # @balance.setter
    # def balance(self, amount):
    #   self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount2()
print(account.balance)  # 0.0
# account.balance = -1 # This would give ERROR: Cannot assign to attribute "balance" for class "BankAccount"
account.deposit(1.99)
print(account.balance)  # 1.99
account.withdraw(1)
print(account.balance)  # 0.99