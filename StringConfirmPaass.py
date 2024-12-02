pass1=input('enter  password:')
pass2=input('confirm password:')

if pass1==pass2:
    print(' you are entered correct password')
else:
    if pass1.casefold()==pass2.casefold():
     print('check the cases and try again')
    else:
     print('password not matching')