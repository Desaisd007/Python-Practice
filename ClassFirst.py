class Cuboid:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h

    def lidarea(self):
        return self.length*self.breadth

    def total(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)

    def volume(self):
        return self.length*self.breadth*self.height


c1=Cuboid(10,5,4)
# here c1 is refers as self
print(c1.lidarea(),c1.volume())

c2=Cuboid(20,10,5)
# here c2 is refers as self
print(c2.total())

