# Find the number of occurrences of each item.
list1 =[x for x in input('enter characters in list, separated by space : ').split()]
result=[]
for item in list1:
    if item not in result:
        result.append(item)
        count=list1.count(item)
        result.append(count)

print(result)