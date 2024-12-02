number=int(input('enter a number:'))
bin=''

while number>0:
   rem=number%2
   number=number//2
   bin = str(rem) + bin

print(bin)