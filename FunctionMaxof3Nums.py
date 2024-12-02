# Find Max of Three Numbers

def big(a,b,c):
    if a>b and a>c:
        print(a,' is biggest number')
    elif b>c:
        print(b,' is biggest number')
    else:
        print(c,' is biggest number')

c = int(input('enter a first number : '))
d = int(input('enter a second number : '))
e = int(input('enter a third number : '))
big(c,d,e)