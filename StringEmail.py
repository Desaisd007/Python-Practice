email_id=input('enter email.id : ')
atrate=email_id.find('@')

print('userId :',email_id[:atrate])
print('domain :',email_id[atrate+1:])