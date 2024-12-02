# here we create shape class with inherirtance
import math


class Polygone:
    def __init__(self,ns,*sides):
        self.No_of_size=ns
        self.sides=sides[:ns]


class Triangle(Polygone):
    def __init__(self,ns,*sides):
        Polygone.__init__(self,ns,*sides)

    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area= math.sqrt((s*(s-a)*(s-b)*(s-c)))
        return area

t1=Triangle(5,10,8,9,5,7)
print('Area', t1.area())