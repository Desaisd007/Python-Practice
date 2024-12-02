import FilePickleStudent,pickle
with open('students.data','rb') as f:
    for i in range(1):
        s = pickle.load(f)
        s.display()