# here we create file using write mode

file=open('MyFirst.txt','w+')
file.write('hey, there !!\n')
file.write('how are you ?\n')
file.write('do you know python\n')

print(file.read(10))

# after closing goto terminal
# then type 'dir' there it show all files name
# then write 'type'+filename it show contents in file.

# file=open('MyFirst.txt','r')
# str2=file.read()
# print(str2)