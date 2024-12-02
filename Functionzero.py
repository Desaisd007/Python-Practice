# find the sum of Scores Ending with Zero
def sum(L):
 addition=0
 for i in range (len(L)):
       if L[i]%10==0:
           addition+=L[i]
       return addition

l=[10,20,30,40,50]
print(sum(l))
