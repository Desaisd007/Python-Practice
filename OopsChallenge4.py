# here we create class for employee using instance and class variable

class Employee:
    count=0
    def __init__(self,Emp_id,name,salary,designation):
        self.Emp_id=Emp_id
        self.name=name
        self.salary=salary
        self.designation=designation
        Employee.count += 1

    def add(self,eid,nam,sal,desi):
        self.Emp_id=eid
        self.name=nam
        self.salary=sal
        self.designation=desi
        Employee.count+=1

    def show(self):
        print('\nEmpId:',self.Emp_id,'\nName :',self.name,'\nsalary:',self.salary,'\ndesignation :',self.designation)
        print(Employee.count)

e1=Employee(1008,'rajaram',25000,'MD')
e1.show()

e1.add(107,'renuka',50000,'CEO')
e1.show()