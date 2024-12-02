
def invDic(d1):
    newd={}
    for k,v in d1.items():
        newd[v]=k
    return newd

fruits = {"apple": 3,"banana": 5,"orange": 2,"mango": 4}
print(fruits)
k= invDic(fruits)
print(k)
