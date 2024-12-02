# here we do practical of instance/class/static variables and methods.
class Demo:
    count=0
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        Demo.count+=1

    def area(self):
        Demo.count += 2
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    # in that class method we can access only class variables.
    @classmethod
    def democount(cls):
        print(cls.count)

    # belows static method doesn't use class or instance variables
    @staticmethod
    def issqure(len,bre):
        return len==bre

c1=Demo(15,5)
print(c1.area())
# below two lines. we can access class variable with classname,and we call class method with instance name
print(Demo.count)
c1.democount()
# below two lines. we can access static method  with classname,and we call class method with instance name
print(Demo.issqure(10,10))
print(c1.issqure(10,10))
