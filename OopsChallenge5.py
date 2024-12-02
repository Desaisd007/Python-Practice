# here we write static function for create calculator
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return abs(a-b)

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def div(a,b):
        return a/b


a=int(input('enter value : '))
b=int(input('enter value : '))
print(Calculator.div(a,b))
print(Calculator.mul(a,b))

