class Student:
    def __init__(self,roll,name,dep):
        self.roll=roll
        self.name=name
        self.dep=dep

    def display(self):
        print(f'Roll:{self.roll} \nName:{self.name}\ndep:{self.dep}')
