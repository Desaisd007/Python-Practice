number=int(input('enter a number :'))
counter=0
while number>0:
   number=number//10
   counter += 1

print(counter)