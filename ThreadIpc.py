# here we learn about concept IPC
from operator import truediv
from threading import *
from time import sleep


class My_data:
    def __init__(self):
        self.data=0
        self.flag=False
        self.lock=Lock()

    def put(self,d):
        while self.flag!=False:
            pass
        self.lock.acquire()
        self.data=d
        self.flag=True
        self.lock.release()
        sleep(1)

    def get(self):
        while self.flag!=True:
            pass
        self.lock.acquire()
        x=self.data
        self.flag=False
        self.lock.release()
        sleep(1)
        return x

def producer(data):
    i=1
    while True:
        data.put(i)
        print('producer',i)
        i+=1

def consumer(data):
    while True:
        x=data.get()
        print('consumer',x)

data=My_data()
t1= Thread(target=lambda:producer(data))
t2=Thread(target=lambda:consumer(data))

t1.start()
t2.start()


t1.join()
t2.join()