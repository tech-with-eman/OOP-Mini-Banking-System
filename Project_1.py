class InvalidTransactionError(Exception): #exception class
    pass
class Account:
    def __init__(self, name):
        self.name = name

class SavingsAccount(Account):  #inheritance
    def __init__(self, name, initial_balance):
        super().__init__(name)
        self.initial_balance = initial_balance

    @property #getter
    def initial_balance(self):
        return self._initial_balance
    @initial_balance.setter  #setter
    def initial_balance(self, value):
        if value < 0:
            raise InvalidTransactionError("Balance cannot be negative.")
        else:
            self._initial_balance = value
    def __str__(self): #str method
        return f"Savings Account | Holder: {self.name} | Balance: {self.initial_balance}"
    def deposit(self, amount):
        if amount < 0:
            raise InvalidTransactionError("Invalid Amount!")
        else:
             self.initial_balance += amount
             return("Deposit Successful!")
    def withdraw(self, amount):
        if amount > self.initial_balance:
            raise InvalidTransactionError("Insufficient Balance!")
        else:
            self.initial_balance -= amount

class CheckingAccount(Account):
    pass
    

account = SavingsAccount("Bob", 500)
account.deposit(50)
account.withdraw(500)
print(account)
        
