# here we create class for bank account using own exception and class variables

class MinBalance(Exception):
    pass

class BankAccount:
    AccountNumber=[]
    Account_counter=1000
    Account_min=3000
    def __init__(self,name,balance=1000):
        self.name=name
        self.balance=balance
        self.account_number=BankAccount.Account_counter
        BankAccount.Account_counter+=1
        BankAccount.AccountNumber.append(self.account_number)



    def deposite(self,acc_no,amount):
        if acc_no in self.AccountNumber:
            self.balance=self.balance+ amount
        else:
            print('Invalid Account Number')

    def withdraw(self,acc_no,amount):
        if acc_no in self.AccountNumber:
            if self.balance < BankAccount.Account_min:
                raise MinBalance("Minimum balance must be maintained.")
            elif amount>self.balance:
                print('insufficient fund !!!')
            else:
                self.balance-=amount

    def show_details(self):
        print ('Account Number :',self.account_number)
        print('Account Name :',self.name)
        print('Account Balance :',self.balance)

bank=BankAccount('satyajeet',5000)
# bank.withdraw(1000,2000)
# bank.withdraw(1000,1000)
bank.withdraw(1000,3200)
bank.withdraw(1000,200)
bank.show_details()
