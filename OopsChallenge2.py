# here we create a circle for class.

class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print ('area of circle is ',(Circle.PI*self.radius**2) )


    def perimeter(self):
        print ('perimeter of circle is ',(2* Circle.PI* self.radius))


c1=Circle(7)
c1.area()
c1.perimeter()