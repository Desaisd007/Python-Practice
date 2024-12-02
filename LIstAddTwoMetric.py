# def add(item,L=[]):
#     L.append(item)
#     return L
#
# add(25)
# add(50)
# add(75)
# l1=[1,5,6,9]
# add(9,l1)
# print(l1)
# print(add(100))

# def add(a,/,e,*,f):
#     return e*f
#
# print(add(6,e=6,f=4))

# def fun(a,b,c):
#     return a+1,b+1,c+1
#
# x,y,z=fun(10,20,30)
# print (x)


# def fun(a,b,c):
#      return a+1,b+1,c+1
#
# l1=[15,16,17]
# t=fun(*l1)
# print(t,type(t))


# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# fun(name='rajat',roll=60,addrress='mumbai')


def fun(**kwargs):
   for i in kwargs:
       total_length=30
       rem=total_length-(len(i) + len(str(kwargs[i])))
       # len dont work on int thats why typecast as a str in above line
       fill=rem*'.'
       print(i,fill, kwargs[i])
fun(name='Rajat',roll=60,address='Mumbai')