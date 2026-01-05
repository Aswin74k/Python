# #arithmetic
a=7
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor division
print(a%b)
print(a**b)

# # is operator

x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
print(x is z)


#Membership operator

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)
print("mango" not in fruits)
print("a" in "banana")
print("X" not in "banana")



#string

word = "world"

print(word[0])
print(word[-1])
print(word[1:4])
print(word[:3])
print(word[2:])
print(word[0:5:2])
print(word[::-1])


word2 = "hello"
print(word[4:2:-1])
print(word+word2)
print(word*3)

#list

list1 = ["apple", 1, 3, 4.5, "banana", True, 6, 7, 8.3, "apple"]
list2 = [12, 13, "orange"]

list5 = []
list4 = list()
list6 = list((1,2,3))
print("list6:", list6)
print("list[0]:", list[-1])
print("lsit[-1]:", list1[:4])
print("list1[2:]:", list[2:])
print("list1[2:5]:", list[2:5])
print("list1[::-1]:", list[::-1])

print("list1 + list2:", list1 + list2)



#tuple
# Reassignment not allowed

tuple1 = ("apple", 1, 3, 4.5, "banana", True, 6, 7, 8.3, "apple")
tuple2 = (12, 13, "orange")

tuple5 = ()
tuple4 = tuple()
tuple6 = tuple([1,2,3])
print("tuple6:", tuple6)
print("tuple[0]:", tuple[-1])
print("tuple[-1]:", tuple1[:4])
print("tuple1[2:]:", tuple[2:])
print("tuple1[2:5]:", tuple[2:5])
print("tuple1[::-1]:", tuple[::-1])

print("tuple1 + tuple2:", tuple1 + tuple2)


#Dictionary

student = {"name": "aswin", "age": 21, "grade": "A"}
print(student["name"])
student["age"] = 22
student["course"]= "CS"

student2 = {
    "name": "head",
    "age": 20,
    "course": "CS"
}

print(student2["name"])
print(student2.get("age"))
print(student2.keys())
print(student2.values())



#Set
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "banana", "cherry"}
set3 = set([1, 2, 2, 3, 4])
print("set3", set3)

set1.add(6)
print("After add:" set1)
set1.remove(3)
print("After remove:", set1)
set1.discard(10)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:" a|b)
print("Intersection:")
