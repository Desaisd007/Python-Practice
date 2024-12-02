number=int(input('enter a number : '))
result=0
while number>0:
    rem=number%10
    result=result*10+rem
    number=number//10

print('reverse number is',result)
