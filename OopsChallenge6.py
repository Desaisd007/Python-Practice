# here we create a function for convertcurrency using get and set

class ConvertCurrency:
    def __init__(self,name,rate):
        self.currency=name
        self.rate=rate

    def setCurrency(self,nm):
        self.currency=nm
    def setRate(self,rt):
        self.rate=rt

    def getCurreny(self):
        print(self.currency)
    def getRate(self):
        print(self.rate)

    def convert(self,amount):
        return str(amount) + self.currency + ' conversion is '+ str (self.rate*amount)


c1=ConvertCurrency('USD',82)
print(c1.convert(3100))