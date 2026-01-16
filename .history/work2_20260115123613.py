class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        print(f"{amount} withdrawn successfully")

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Balance:", self.balance)

try:
    acc = Account("Aswin", 5000)
    acc.display()
    acc.deposit(2000)
    acc.withdraw(10000)   
    acc.display()

except InsufficientBalanceError as e:
    print("Error:", e)

