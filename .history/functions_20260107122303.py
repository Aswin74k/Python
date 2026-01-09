
# def greet():
#     print("Hello, Guys!")
# greet()    

# #Function with parameters
# def greet(name):
#     print(f"Hello, {name}")
# greet("head")   
# greet("smith") 


#Function to add two numbers

# def add(num1,num2):
#     print(num1+num2)
#     return num1+num2

# add(2,5)
# add(40,20)
# x=10
# y=60
# add(x,y)
# res=add(x,y)
# print(res)


#Function of find sum of 1 to n numbers
# def print_num(n):
#     sum=0
#     for i  in range(1,n+1):
#         sum+=i
#     return sum    
# total=print_num(20)  
# total2=print_num(60)   
# print(f"total : {total}")
# print(f"total : {total2}")



def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

f1 = fact(5)
f2 = fact(7)

print(f"Factorial : {f1}")
print(f"Factorial : {f2}")


def revrse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //=10
        
