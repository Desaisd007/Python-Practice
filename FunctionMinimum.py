# write function for Minimum Variable Number

def minimum(*value,low_limit=None):
    if low_limit is None:
        return min(value)
    else:
        L=[x for x in value if x>=low_limit]
        return min(L)

print(minimum(10,35,9,8,59,95,48,low_limit=15))
print(minimum(10,35,9,8,59,95,48))

