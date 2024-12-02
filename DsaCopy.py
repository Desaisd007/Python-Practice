# This is useful for duplicating the objects.This module is having two methods.
# One is copy which will do shallow copy of the object and one more is deep copy of the object.

import copy
L=["apple", "banana", "cherry", "lichi", "guava"]

# now we create shallow copy of list
L1=copy.copy(L)
print(L1)
print(id(L))
print(id(L1))
print(id(L[0]))
print(id(L1[0]))
# here we create shallow copy . address of list are diff. but address of object in both list are same.

# now we create deepcopy of list
L2=copy.deepcopy(L)
print(L2)
print(id(L))
print(id(L2))
print(id(L[0]))
print(id(L2[0]))

