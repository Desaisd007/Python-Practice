number=int(input('enter a number :'))
number1=number
result=0
while number>0:
    rem=number%10
    result=result*10+rem
    number=number//10

if result==number1:
    print(number1 ,'number is palindrome')
else:
    print(number1, 'number is not palindrome')