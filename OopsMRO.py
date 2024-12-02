class A:
    def show(self):
        print('A show method')

class B:
   pass

class C(A,B):
    pass

c=C()
c.show()
print(C.mro())