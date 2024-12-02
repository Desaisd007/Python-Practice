# here we perform operations on file

file=open('MyFirst.txt','r+')
str1=file.read(20)
print(str1)
file.write('python is very interesting language')
file.close()