# create a class account with attributes name and balance 
# methods deposit withdraw display
# raise custom exception for insufficient balance

# Custom Exception
class InsufficientBalanceError(Exception):
    pass


# Account Class
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully")

    # Withdraw method with custom exception
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully")

    # Display method
    def display(self):
        print("\nAccount Holder:", self.name)
        print("Balance:", self.balance)


try:
    acc = Account("Aswin", 5000)

    acc.display()
    acc.deposit(2000)
    acc.withdraw(10000)   # This will raise exception
    acc.display()

except InsufficientBalanceError as e:
    print("\nError:", e)

finally:
    print("\nProgram execution completed")
     

