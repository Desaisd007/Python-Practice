def div():
    try :
        a = int(input('enter any number :'))
        b = int(input('enter any number :'))
        c=a//b
        return c
    except (ZeroDivisionError,TypeError) as err:
        raise (ZeroDivisionError,TypeError)
    finally:
        print('finally block executed')


e=div()
print(e)