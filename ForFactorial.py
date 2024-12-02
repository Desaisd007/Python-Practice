number=int(input('enter a number :'))
result=1
for i in range(number,1,-1):
    result=result*i

print('factorial of',number,'is',result)