import sqlite3
conn = sqlite3.connect('univ.db')
# that connect command is connect database if it is exist.
# else create new db

cur=conn.cursor()
# here we create cursor

# using cur.execute we create tables.
cur.execute('create table dept( deptno integer primary key,dname text)')
cur.execute('create table student(roll integer primary key,name text,city text,deptno integer,foreign key(deptno) references Dept(deptno))')

conn.commit()
cur.close()
conn.close()