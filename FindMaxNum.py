num_of_nums=int(input('enter the rotation number :'))
max=0
count=0

while count<num_of_nums:
    n=int(input('enter the numbers : '))
    if n>max:
        max=n

    count+=1

print('maximum number is :' , max)