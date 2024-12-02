#rearranging upper and lower cases wise.

str1=input('enter a string : ')
lower=''
upper=''

for x in str1:
    if x.islower():
        lower+=x
    else:
        upper+=x

print(lower+upper)