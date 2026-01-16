# -------------------error handling
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
result = num1 / num2

print(f"{num1} / {num2} = {result}")


try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except zerodivisionError:
    print("can't divide by zero")
except valueError:
    print('Invalid input')    
else:
    print("division successfull")      


#  using file handling
try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 / num2

except ZeroDivisionError:
    with open("read.txt", "w") as file:
        file.write("Error: Can't divide by zero\n")
    print("Can't divide by zero")

except ValueError:
    with open("read.txt.txt", "w") as file:
        file.write("Error: Invalid input. Please enter numbers only\n")
    print("Invalid input")

else:
    with open("read.txt", "w") as file:
        file.write(f"{num1} / {num2} = {result}\n")
    print("Division successful")

finally:
    print("Program execution completed")



try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age < 18:
        raise Exception("Not eligible to vote")

except ValueError:
    print("Invalid input! Please enter a valid number.")

except Exception as e:
    print(e)

else:
    print("You are eligible to apply for vote ")

finally:
    print("Thank you for using the voting system")

# ------custom Exception and raising error
class AgeError(Exception):
    pass
try:
    age = 17
    if age < 18:
        raise AgeError("Age must be 18")
except AgeError as e:
    print(e)  

class Balance(Exception):
    pass
try:
    balance = 30
    if balance > 18:
        raise Balance("low balance")
except Balance as e:
    print(e)  

try:
    num = int(input("Enter a number: "))
    result = num ** 2
    print(f"Square of {num} = {result}")

except ValueError:
    print("Invalid input")

else:
    print("Squaring successful")