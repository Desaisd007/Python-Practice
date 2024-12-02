mylist1=[x for x in input('enter a elements for create list, separated by space : ').split()]
mylist2=[]

for x in mylist1:
    if x not in mylist2:
        mylist2.append(x)

print(mylist2)
