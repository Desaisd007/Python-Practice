# here we create a inner class for student and school

class School:
    def __init__(self,SchoolNam,name,age,grades):
        self.SchoolName=SchoolNam
        self.Student=self.Student(name,age,grades)
    class Student:
        def __init__(self,name,age,grade):
            self.name=name
            self.age=age
            self.grade=grade

        def display(self):
            print(self.name,'\n',self.age,'\n',self.grade)

c = School('Dvm','satyajeet',16,'A+')
c.Student.display()