# Counter is apart of the collections module and is used to count the occurrences of elements in an iterable, such as a
# list or string.It creates a dictionary - like object where keys are the elements, and values are their counts.
from collections import Counter

L=["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve", "Charlie"]
coun = Counter(L)
print(coun)

# here we get Alice count
a=coun['Alice']
print(a)

b=coun.get('Alice')
print(b)

# counter create dict .now we get all keys and values separately
a=coun.keys()
print(a)

b=coun.values()
print(b)

# now we update dict
coun.update({'ajay':4})
print(coun)

# we perform for loop on dict
coun.elements()
for i in coun.elements():
    print(i)


# now we remove the content
coun.pop('Alice')
print(coun)

# now we remove very 1st content in dict
coun.popitem()
print(coun)

# now we find most common(which count is more) element in dict
print(coun.most_common(1))
# most common 1st two
print(coun.most_common(2))
