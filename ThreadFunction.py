# here we write code for create thread using function

from threading import *
from time import *

def display():
    for i in range(65,91):
        print(chr(i))
        sleep(1)

# t = Thread(target=lambda:display())
t = Thread(target=display,name='Alphabet')
t.start()

for i in range(65,91):
    print(i)
    sleep(1)
t.join()

