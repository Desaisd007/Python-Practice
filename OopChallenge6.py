# here we write function for phone number using accessors and mutators

class Phone_no:
    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no

    def getName(self):
        return self.name
    def getPhone_no(self):
        return self.phone_no

    def setName(self,nm):
        self.name=nm
    def setPhone_no(self,ph):
        self.phone_no=ph

    def display(self):
        print('\nName : ', self.name,'\nPhone_No : ',self.phone_no)

ph_no=Phone_no('Abhijit','7895648977')
ph_no.display()
print(type(ph_no),'    ',id(ph_no))

ph_no.setName('Rahul')
ph_no.setPhone_no('7896489700')
ph_no.display()
print(type(ph_no),'    ',id(ph_no))
