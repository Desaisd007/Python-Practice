# l1={10,20,30,40,50}
# l2={10,20}
# l3=l1.copy()
# print (l3)
import time
from datetime import datetime
from email.utils import decode_params
from idlelib.query import Query
from queue import Queue

# l1=[10,20,30,40,50]
# print(l1)
# l1.reverse()
# t1=()
# for i in l1:
#     t1+=(i,)
# print(t1)

# class Parent():
#
#     def show(self):
#         print('parent show called')
#
#     def display(self):
#         print('parent display called')
#
#
# class Child(Parent):
#     def show(self):
#         print('child show called')
#
#     def display(self):
#         print('child display called')
#         super().display()
# c=Child()
# c.show()
# c.display()
# p=Parent()
# p.show()


# l1=[10,20,30,40,50]
# print(l1.remove(40))
# print(l1)

# t1=(10,20,30,40,50)
# print(id(t1))
# t1=26,45,158,
# print(id(t1))
# print(t1)


# l1={10,20,30,40,50}
# itr=iter(l1)
# print(next(itr))
# print(next(itr))

# e=10
# def upd(a,b,d):
#     c=a+b
#     print(c)
#     e=d
#     print(e)
# upd(10,15,20)

# def outer():
#     def inner():
#         print('hello world')
#     return inner()
# outer()

# print(dir(Queue))

# import time
# import datetime
# print(time.time())
# print(time.localtime())
# print(datetime.datetime.now())


def decorator( fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('+' * 10)
    return wrapper


# @decorator
def display(msg):
    print(msg)

d=decorator(display)
d('vanakkam')