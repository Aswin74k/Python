file = open('sam.txt','w')
file.write("hello guys")
file.close()


file = open('sam.txt','a')
file.write("Append text")
file.close()


file = open('sam.txt','r+')
file.write("Good <Morning")
file.close()

file = open('sam.txt','r')
content = file.read()
print(content)
file.close()


