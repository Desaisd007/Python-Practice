number=int(input('enter a number : '))

while number>0:
    result=number%10
    number=number//10
    print(result)