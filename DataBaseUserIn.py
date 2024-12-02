import sqlite3

conn=sqlite3.connect('univ.db')
curr=conn.cursor()

# we are taking input from user
dno=int(input('Enter Department No:'))
dname= input('Enter Department name : ')

# passing that input using format
curr.execute(f"insert into dept values ({dno},'{dname}')")

conn.commit()
curr.close()
conn.close()