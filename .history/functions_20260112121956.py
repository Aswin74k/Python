
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



# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# f1 = fact(5)
# f2 = fact(7)

# print(f"Factorial : {f1}")
# print(f"Factorial : {f2}")

#Reverse of a number
# def reverse_num(n):
#     rev = 0
#     while n > 0:
#         rev = rev * 10 + n % 10
#         n //=10
#     return rev
# num = int(input("Enter the number:"))   
# print(reverse_num(num))
# print(reverse_num(345))



#Default parameters
# def greet(name="Guest"):
#     print("Hello", name)
# greet()
# greet("Aswin")  

# #keyword argument
# def student(name, age, is_student=True):
#     print("Name:", name, "Age:", age, "is student",is_student)
# student(20,"Aswin",True) 

# student(is_student=False,age=20,name="Aswin")
# student("virat",37)


#variable number of Arguments

# def total(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
# print(total(2, 4, 6))
# print(total(2,4))
# print(total(2, 4, 6,7,8,9)) 


# def show_students(*students):
#     for i, student in enumerate(students, start=1):
#         print(f"\nStudent {i}:")
#         for key, value in student.items():
#             print(key, ":", value)

# show_students(
#     {"name": "Aswin", "age": 20, "grade":"A+"},
#     {"name": "Head", "age": 35, "grade":"A"},
#     {"name": "Smith", "age": 37, "grade":"O"}
# )



# Built-in function

# s = "cricket"
# print("string:", s)
# print("Length:", len(s))
# print("upper:", s.upper())
# print("lower:", s.lower())
# print("title:", s.title())
# print("capitalize:", s.capitalize())
# print("casefold:", s.casefold())
# print("swapcase:", s.swapcase())

# # change case

# s = "Python String and variable"
# print("")


# Strip Lstrip Rstrip

# s = "Hello\nWorld"
# print(s)
# print(repr(s))
#  s = "Hello python"
#  print("original:", rep(s))
#  print("strip:", repr(s.strip))












# Replace substring
# s = "Wello World Hello World"
# print("original:", s)
# print("Replace 'World' with 'python':", s.replace("world", "python"))
# print(s)#original string


#split/join

# s = "apple, banan, cherry"
# print("Original", s)
# print("split by comma:", s.split(","))

# words = ["python", "is", "fun"]
# print("join with space:", " ".join(words))


# Find / rfind / index

# s = "Hello world"
# print("find 'o':", s.find("o"))
# print("Rfind 'o':", s.rfind("o"))
# print("Index 'W':", s.index("w"))


# Count occurrences
# s = "banana"
# print("Count 'a':", s.count("a"))

#Start / End check

# s = "python"
# print("Start with 'py':", s.startswith("pyt"))
# print("End with 'on':", s.endwith("on"))


#Check type of characters

# s1 = "Hello"
# s2 = "123"
# s3 = "Hello123"
# s4 = " " 
# print("s1.isalpha():", s1.isalpha()) 
# print("s2.isdigit():", s2.isdigit()) 
# print("s3.isalnum():", s3.isalnum()) 
# print("s4.isspace():", s4.isspace()) 
# print("s1.istitle():", s1.istitle()) 
# print("s1.isupper():", s1.isupper()) 
# print("s1.islower():", s1.islower())


#Padding and alignment

# s = "42"
# s2="567"
# print("zfill(5):", s.zfill(5)) 
# print("zfill(5):", s2.zfill(5)) 
# print("center(20, ' '):", s.center(20, ' '))
# print("ljust(20, '-'):", s.ljust(20, '-')) 
# print("rjust(20, '-'):", s.rjust(20, '-'))



# s = "Hello-world-python"
# print("partition by '-':", s.partition("-"))
# print("Rpartition by '-':", s.rpartition("-"))



# fruits = ["appe", "banana"]
# fruits.append("cherry")
# print("Append:", fruits)

# fruits.insert(1, "mango")
# print("Insert:", fruits)

# fruits.extend(["grapes", "orange"])
# print("Extend:", fruits)




# Removing elements
# fruits = ["apple", "banana", "cherry", "apple"]
# fruits.remove("apple")
# print("remove:", fruits)
# fruits.pop()
# print("pop last:", fruits)
# fruits.pop(0)
# print("pop index 0:", fruits)
# fruits.clear()
# print("clear:", fruits)


# # sorting and reverse
# nums = [3, 1, 4, 2]
# nums.sort()
# print("sorted accending:", nums)

# nums.sort(reverse=True)
# print("sorted decending order:", nums)

# nums.reverse()
# print("reverse:", nums)

# Copying





# Lamda functon
# add = lambda a,b : a + b
# print(add(10,20))


# cube = lambda n: n ** 3
# print(cube(7)) 



# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *=i
# print(fact)    

# # function with recursion
# def factorial(n):
#     if n==1:
#         return n
#     return n * factorial(n-1)
# print(factorial(5)) 


# def fibonacci(n):
#     if n<1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)  
# print(fibonacci(6))  

import math
print(math.sqrt(25))






