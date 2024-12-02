# here we learn about threading using IPC queue

from threading import *
from time import*
from queue import *


q = Queue()

def producer(q):
    i=1
    while True:
        q.put(i)
        print('producer :', i)
        i+=1
        sleep(1)

def consumer(q):
    while True:
        x=q.get()
        sleep(1)
        print('consumer',x)

t1=Thread(target=lambda:producer(q))
t2=Thread(target=lambda:consumer(q))

t1.start()
t2.start()
t1.join()
t2.join()
