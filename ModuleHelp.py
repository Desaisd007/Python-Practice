
total_amount =2000

def add(a,b):
    return a+b

def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a


if __name__=='__main__':
 print(__name__)
 c=int(input('enter 1st number : '))
 d=int(input('enter 2nd number : '))
 print(add(c,d))
 print(sub(c,d))
 print(total_amount)