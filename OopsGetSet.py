class OopsGetSet:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def getLength(self):
        return self.length

    def getBreadth(self):
        return self.breadth

    def setLength(self,l):
        self.length=l

    def setBreadth(self,b):
        self.breadth=b

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

o1=OopsGetSet(15,5)
print('before set call area is ',o1.area())
o1.setLength(10)
print('after set call area is ',o1.area())
print(o1.getLength())