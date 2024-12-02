# 1st create simple function
# def miles(num):
#     return 1.6*num
#
# print('kms', int(miles(10)))
# its lambda is
# k = lambda miles:1.6*miles
# print('kms', int(k(10)))

# def add(a,b):
#     return a+b
# print(add(5,4))
# its lambda is
# m =lambda a,b:a + b
# print(m(5,4))

f= lambda a,b:a if a>b else b
print(f(5,6))