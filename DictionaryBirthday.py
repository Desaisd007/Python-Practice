birthdays={'Rahul': '27/24/2003','Sia':'11/09/1999','Rohan':'24/28/2009'}
name=input('enter name for getting DOB : ')
name2=name.title()

if name2 in birthdays:
 print(name2,birthdays[name2])
else:
    print('not found')