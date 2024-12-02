# here we write function for threads using semaphore

from threading import *
from time import *


def display(str1):
    # here we use acquire method of lock class. which lock particular thread in that function
    l.acquire()
    for i in str1:
        print(i)
        # sleep use for control printing speed of thread
        sleep(1)
    # here we release that lock and then only next thread comme in that function
    l.release()

# here we create object of semaphore class. 2 means 2 threads are at a time
l= Semaphore(2)

# here we call the methods of thread clas
t1=Thread(target=display,args=('HELLO WORLD',))
t2=Thread(target=display, args=('how aare you?',))
t3=Thread(target=display, args=('what is your name?',))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()