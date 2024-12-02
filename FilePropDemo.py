#1] if you want to read all file as a single string
# file=open('prop.txt','r')
# str2=file.read()
# print(str2)
# file.close()

#2]when we want to read one line or line by line
# file=open('prop.txt','r')
# line=file.readline(end=' ')
# print(line)
# file.close()

# 3]readlines method read all lines and print it in the form of string
# file=open('prop.txt','r')
# lines=file.readlines()
# print(lines)
# file.close()
#
# if you wants to print lines one by one using readlines then
# file=open('prop.txt','r')
# lines=file.readlines()

# for line in lines:
#     print(line,end='')
# file.close()
# ------------------------------------------------------------------------------
# write methods
# if want to write in existing file or wants to create new line and write then use write
# file= open('prop.txt','w')
# file.write('vanakam')
#
# if we wants to write multiple lines in code
file= open('prop.txt','w')
list1=['my name is ramesh\n','i am from mumbai\n','i worked as a data engineer\n']
file.writelines(list1)

