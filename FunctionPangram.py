def pangram(phrase):
    s={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '0', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    phr=set(phrase)
    if len(phr)>=len(s):
        print('this is pangram')
    else:
        print('this is not pangram')

str1=str(input('enter sentense:').split(' '))
pangram(str1)
