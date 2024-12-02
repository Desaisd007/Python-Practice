# print fact using recursion
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))

# print sum of 10 to 1 using recursion
# def sum(n):
#     res=0
#     if n==0:
#         return res
#     else:
#      return  n+sum(n-1)
# print(sum(10))

# print name 10 times using recursion
# count=1
# def printer(name):
#     global count
#     if count < 11:
#         print(count,'.',name)
#         count = count + 1
#         printer(name)
#
# printer('satyajeet')

#power of number using recursion
# def power(a,b):
#    if b==0:
#        return 1
#    else:
#        return a*power(a,b-1)
#
# print(power(2,5))


#prime number program using recursion
# def prime(a,b):
#     if b==1:
#         return 1
#     if a%b==0:
#         return 0
#     return prime(b,b-1)
#
# a=int(input('Enter a Number : '))
# count=prime(a,a-1)
# if count==1:
#      print(a ,' is prime')
# if count==0:
#     print(a,' is not prime')


#count total digits in number
count=0
def digits(n):
    global count
    if n<=0:
       return count
    else:
        if n%10:
            count=count+1
            n=n//10
            return digits(n)

b=int(input('enter a number: '))
print('total digits :',digits(b))
