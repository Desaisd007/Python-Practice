# Here we create outer class course and inner class books


class Course:
    def __init__(self,name,duration,*books):
        self.course_name=name
        self.duration=duration
        self.books=[self.Book(b) for b in books]


    def show_details(self):
        print('Name :',self.course_name)
        print('duration :',self.duration)
        print('suggested books :')
        for b in self.books:
            print(b)

    class Book:
        def __init__(self,title):
            self.title=title

        def __str__(self):
            return self.title

c1=Course('Python',6,'Learn  python','python 365','Easy Python')
c1.show_details();