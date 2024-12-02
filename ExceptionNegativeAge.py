class NegativeAgeException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return 'Age are Not Negative'

def NegativeAge(age):
    if age<0:
        raise NegativeAgeException
    elif age>=0 and age<13:
        print('kid')
    elif age>=13 and age<19:
        print('teen')
    elif age>=19 and age<50:
        print('young')
    else:
        print('old')

number=int(input('enter age : '))

try:
    NegativeAge(number)
except NegativeAgeException as e:
    print(e)
