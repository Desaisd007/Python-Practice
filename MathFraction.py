import fractions
# we create fraction using integers
f1=fractions.Fraction(1,2)
print(f1)

# we create fraction using float number
f2= fractions.Fraction(0.9)
print(f2)

# we create fraction using string
f3=fractions.Fraction('3.3')
print(f3)

# now we use limit_denominator
f4=f2.limit_denominator(10)
print(f4)

# we can do add/sub/mul/del on fraction
print('add' ,f1+f4)
print('sub' ,f1-f4)

# finding  numerator and denominator
print(f1.numerator)
print(f4.denominator)

# list of tuple converts into fractions
L=[(1,3),(2,5),(5,6)]

for n,d in L:
    print(fractions.Fraction(n,d))