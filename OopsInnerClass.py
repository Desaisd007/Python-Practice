# here we learn concept of inner class.
from email.headerregistry import Address


class Customer :
    def __init__(self,uid,name,bno,bstreet,bcity,bcountry,bpin,sno,sstreet,scity,scountry,spin):
        self.uid=uid
        self.name=name
        self.baddr=self.Address(bno,bstreet,bcity,bcountry,bpin)
        self.saddr=self.Address(sno,sstreet,scity,scountry,spin)

    class Address:
        def __init__(self,dno,street,city,country,pin):
                self.dno=dno
                self.street=street
                self.city=city
                self.country=country
                self.pin=pin

        def display(self):
                print(self.dno)
                print(self.street)
                print(self.city)
                print(self.country)
                print(self.pin)

c=Customer(10,'satyajeet',101,'abc chowk','pune','maharashtra',413001,10001,'xyz','mumbai','maharashtra',412001)
c.saddr.display()