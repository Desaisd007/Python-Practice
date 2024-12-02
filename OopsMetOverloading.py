class Overloading:
    def sum(self,a,b,c=None):
        s=a+b
        if c==None:
            return s
        else:
            return c+s

a=Overloading()
print(a.sum(12,15,10))
print(a.sum(12,15))

        