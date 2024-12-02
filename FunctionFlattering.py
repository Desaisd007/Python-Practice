# write Function for Flattening Nested List using generator

def flattening(L1):
    for i in L1:
        if hasattr(i,'__iter__'):
            yield from flattening(i)
        else:
            yield i

f=flattening([1, 2, 3, [7, 8, 9,[4, 5, 6,[10, 11, 12]]]])

print(next(f))
print(next(f))
print(next(f))
print(next(f))

