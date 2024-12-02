# Concatenating List into Single Number
mylist=[int(x) for x in input('enter a number in list, separated by space : ').split()]
str1=''
print(mylist)
for i in mylist:
    str1+=str(i)

print(int(str1))
