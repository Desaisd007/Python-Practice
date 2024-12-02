import random

n=random.randint(1,10)
guess=0

while guess!=n:
    guess=int(input('enter a number : '))
    if guess<n:
        print('your number is lesser')
    elif guess>n:
        print('your number is bigger')
    else:
        print('You got the number')