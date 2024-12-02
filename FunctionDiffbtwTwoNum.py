# Difference Between Two Numbers if diff is greater than then invalid choice.

def diff(a,b):
    difference=a-b
    if abs(difference)<=5:
        return difference
    else:
        return 'invalid Matching'

a=int(input('enter first number : '))
b=int(input('enter second number : '))
print(diff(a,b))