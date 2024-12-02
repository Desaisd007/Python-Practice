john = float(input('enter johns age : '))
smith = float(input('enter smiths age : '))
ajay = float(input('enter ajays age : '))

if john>smith and john>ajay :
    print('john is eldest')
elif smith>ajay :
    print('smith is eldest')
else:
    print ('ajay is eldest')