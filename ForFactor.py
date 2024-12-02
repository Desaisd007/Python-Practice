n=int(input('enter a number :'))
rem=0
for i in range(1,n,1):
    rem=n%i
    if rem==0:
        print(i)
    else:
        i+=1