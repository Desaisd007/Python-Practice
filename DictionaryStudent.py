student={}

for i in range(3):
    name=input('enter a names : ')
    roll_no=int(input('enter a roll number :'))
    dept =input('enter department :')

    student[roll_no]={'name':name,'dept':dept}

print(student)