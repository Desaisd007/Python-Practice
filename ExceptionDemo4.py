# here we try Nested try & except

try:
    a=int(input('enter a number : '))
    try:
        b=int(input('enter a number : '))
        try:
            c=a//b
        except ZeroDivisionError as err:
            print(err)
        else:
            print(c)
    except:
        print('enter valid number')
except:
    print('enter valid number')