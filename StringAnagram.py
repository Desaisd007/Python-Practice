str1=input('enter string1 : ')
str2=input('enter string 2 : ')
if len(str1)!=len(str2):
    print('that strings are not anagram')
else:
    for x in str1:
        if x not in str2:
            print('that strings are not anagram')
            break
        else:
            print('that strings are anagram')
            break