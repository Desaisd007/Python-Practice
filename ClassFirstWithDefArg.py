#here we pass default arguments to constructor

class Cuboid:
    def __init__(self,l=1,b=1,h=1):
        self.length=l
        self.breadth=b
        self.height=h

    def lid_area(self):
        return self.length*self.breadth

    def total(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)

    def volume(self):
        return self.length*self.breadth*self.height


c1=Cuboid()
print(c1.lid_area())

c2=Cuboid(10)
print(c2.lid_area())

c3=Cuboid(10,20)
print(c3.lid_area())

c4=Cuboid(20,10,5)
print(c4.total())
