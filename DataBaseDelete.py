# here we learn how delete data in database using python program

import sqlite3
conn = sqlite3.connect('univ.db')
cur=conn.cursor()

# here we write query for delete data in database
cur.execute('delete from dept where deptno=60 ')
row=cur.execute('select * from dept')
print(row.fetchall())
conn.commit()
cur.close()
conn.close()