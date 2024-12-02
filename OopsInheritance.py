
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self*breath

    def perimeter(self):
        return 2*(self.length+self.breadth)

class Cuboid(Rectangle):
    def __init__(self,length,breadth,height):
        self.height=height
        super().__init__(length,breadth)

    def volume(self):
        return self.length * self.height * self.breadth


c = Cuboid(15,25,10)
print(c.volume())