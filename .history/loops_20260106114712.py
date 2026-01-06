# while

# i = 1
# while i<=10: 
#     print(i)
#     i+=1

# i = 10
# while i>=1:
#     print(1)
#     i-=10

    #while


# i = 1
# while i<=20:
#     if i%2==0:
#         print(i) 
#     i+=1


# i = 2
# while i<=20: 
#     print(i)
#     i+=2


# sum=0
# i=1
# while i <=10: 
#     sum +=i
#     i+=1
# print(f"sum = {sum}")    


# num=int(input("enter a number:"))
# fact=1
# i=1
# while i<=num: 
#     fact*=i
#     i+=1
# print(f"factorial of {num} = {fact}")


import random

secret_number = random.randint(1, 50)
print("**welcome to the number guessing game!**")
print("guess a number between 1 qnd 50.")
guess = None
attempts = 0

while guess != secret_number:
    guess = inr(input(""))
