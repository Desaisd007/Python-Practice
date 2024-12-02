import FilePickleStudent,pickle
stud =[FilePickleStudent.Student(10,'satya','etc')]
with open('students.data','wb') as f:
    for s in stud:
        pickle.dump(s,f)
