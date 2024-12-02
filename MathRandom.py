# it is inbuilt function having a lot of functions for generating random numbers.
import random

# that random function show random float number in between (0-1)
print(random.random())

# using uniform we can get any random float number between our given range
print(random.uniform(1,10))

# using randint we can get any random int in given range
print(random.randint(1,10))

# using randrange we can get random number in given range with adding steps
print(random.randrange(1,20,3))

# if you want same set of random numbers are repeated then use seed because seed dosent take system time.(random function takes)
random.seed(10)
print(random.random())
print(random.random())
random.seed(20)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
print(random.random())
#NOTE : here we see that using random+ seed it give specific random number as return

# using choice() it can return choice number which only present in given iterable
L=[1,3,5,9,7,6,8]
print(random.choice(L))
# there is one more function choices
print(random.choices(L,k=2))
# sample() function is works like as choices()
print(random.sample(L,k=3))
# shuffle() = change  positions of numbers in iterable
random.shuffle(L)
print(L)


# using getstate() then random.random()  we get  random numbers, then we use set state and again call random.random then get that same numbers
print(random.random())
st=random.getstate()
print(random.random())
print(random.random())
random.setstate(st)
print(random.random())
print(random.random())


# using getrandbits() we can get values in between 2**(what number we enter).
print(random.getrandbits(4))
print(random.getrandbits(4))
print(random.getrandbits(4))