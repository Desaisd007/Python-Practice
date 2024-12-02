# Minimum Index in Sum of Two Lists

list1=[x for x in input('enter list of your favourite food , separated using space : ').split()]
list2=[x for x in input('enter list of your favourite food , separated using space : ').split()]

index1=7
index2=7
for x in range(len(list1)):
     indx=list2.index(list1[x])

     if x+indx < index1+index2:
         index1=x
         index2=indx

print(list1[index1],index1+index2)