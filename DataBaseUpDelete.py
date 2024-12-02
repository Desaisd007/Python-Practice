# Here we write query for updating table

import sqlite3
conn=sqlite3.connect('univ.db')
cur=conn.cursor()

# here we pass query for update table
cur.execute('update dept set name="ETC" where deptno==10')
# here we write query for fetching data databases
row=cur.execute('select * from dept')
print(row.fetchall())
conn.commit()
cur.close()
conn.close()