import sqlite3

# 1st - connect server to db
conn=sqlite3.connect('univ.db')

# 2nd - create cursor
curr= conn.cursor()

# 3rd - execute cursor (where we can write sql query)
curr.execute("insert into dept values(10,'CSE')")
curr.execute("insert into dept values(dname,deptno) values('ECE',20)")

conn.commit()
curr.close()
conn.close()
