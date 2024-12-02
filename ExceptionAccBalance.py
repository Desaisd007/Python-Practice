balance=10000
print('your account Balance is : ' ,balance)

class MinBalanceLimit(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return 'Your balance is at Minimum amount'

def withdraw(amount):
    global balance
    balance= balance - amount
    if balance>=5000:
        return balance
    else:
        raise MinBalanceLimit

amount=int(input('enter amount :'))
try:
    print('Remaining Balance :',withdraw(amount))
except MinBalanceLimit as e:
    print(e)