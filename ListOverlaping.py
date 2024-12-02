# Overlapping Elements in Two Lists

list1=[int(x) for x in input('enter numbers in list:').split()]
list2=[int(x) for x in input('enter numbers in list2:').split()]
list3=[]

for x in list1:
    if x in list2:
        list3.append(x)

print(list3)