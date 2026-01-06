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


# import random

# secret_number = random.randint(1, 50)
# print("**Welcome to the Number Guessing Game!**")
# print("Guess a number between 1 qnd 50.")
# guess = None
# attempts = 0

# while guess != secret_number:
#     guess = int(input("Enter your guess:"))
#     attempts += 1

#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.") 
#     else:
#         print(f"Correct! The number was {secret_number}.")
#         print(f"You gussed it in {attempts}.")       




#for loop
#range(start, stop, step)

# for i in range(11):
#     print(i)

# for i in range(2, 11):
#     print(i)
 
# for i in range(2, 11, 2):
#     print(i) 


# n1 = int(input("Enter a number :"))
# sum = 0
# for i in range(1,n1+1): 
#     sum+=i
# print(sum)

list1=[10,20,30,40]
for i in list1:
    print(i)


for index, value in enumerate(list1): 
    print(index, value)
str1
