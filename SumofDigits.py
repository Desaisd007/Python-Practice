number=int(input('enter a number : '))
sum=0
while number>0:
    remainder=number%10
    sum=sum+remainder
    number=number//10

print('sun of digits :',sum)
