 # Math module having all the mathematical functions builtin functions and some constants are also available.
import math
print(math.ceil(12.1))
print(math.floor(13.5))
print(math.fabs(-15.5))
print(math.fmod(13,5))
print(math.remainder(13,5))
print(math.sqrt(25))
print(math.isqrt(25))
print(math.pow(2,5))
print(math.factorial(5))
# gcd = greatest common factor
print(math.gcd(35,21))
# perm gives permitation (npr) result . ist number must be greater
print(math.perm(5,2))
# comb gives combination (ncr) result . ist number must be greater
print(math.comb(5,2))
# prod() takes iterable only
print(math.prod((10,20)))
# fsum() takes iterable only
print(math.fsum({1,2,3,5,8,8}))

print(math.radians(10))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))

print(math.log(10))
print(math.log10(10))
print(math.log2(10))