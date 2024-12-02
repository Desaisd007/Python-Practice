card_no=input('enter card number: ')
lastdigits=card_no[15::]

four='*' * 4 +' '
dispno=four*3+lastdigits
print(dispno)
