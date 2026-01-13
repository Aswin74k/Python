file = open('sam.txt','w')
file.write("hello guys")
file.close()


file + open('sam.txt','a')
file.write("Append text")
filr

file = open('sam.txt','r')
content = file.read()
print(content)
file.close()


