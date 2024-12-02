# using array data structure in python we create homogeneous type of array
#  syntax: array_name=array.array(type,(array items))

# here we create integer array
import array
ar1 = array.array('i', (10, 20, 30, 40,50))
print(ar1)

# byte type string
s=b'abcdef'
ar2=array.array('b',s)
print(ar2)

# finding element based index
print(ar2[0])
# access the index number
print(ar2.index(102))

# slicing
print(ar2[1:3])

# append
ar2.append(103)
print(ar2)

# count
print(ar2.count(97))

# extend
ar2.extend([105,106,107])
print(ar2)