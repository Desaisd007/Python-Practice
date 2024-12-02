# This maintains a list in the sorted order. also containt duplicates
# Even this data structure doesn't create a new object, but it will perform operations on existing object

import bisect
L=[10,20,20,30,48,49,55,78,98]

# we add new element is list
bisect.insort(L,25)
print(L)
# element automatically add inn sorted order

# add element which already present in current list.depends on where add left of right of present element
bisect.insort_right(L,98)
print(L)
print(id(L[9]))
print(id(L[10]))
# both variable point to same object


bisect.insort_left(L,30)
print(L)



# NOTE: it not create new list , it update the existing list