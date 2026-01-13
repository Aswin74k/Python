file = open('sam.txt','w')
file.write("hello guys")
file.close()


file + open('a')

file = open('sam.txt','r')
content = file.read()
print(content)
file.close()


