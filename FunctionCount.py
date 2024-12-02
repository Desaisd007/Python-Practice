
def count(pharse):
    Usum=0
    Lsum=0
    for i in pharse:
        if i.isupper():
            Usum+=1
        elif i.islower():
            Lsum+=1
    print('uppercases: ',Usum,'and lowercases :',Lsum)

str1=str(input('enter a string :').split(' '))
count(str1)