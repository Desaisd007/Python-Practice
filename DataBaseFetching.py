import sqlite3

# -------------------------------------------
# conn=sqlite3.connect('univ.db')
# curr=conn.cursor()
#
# # here we access data of rows
# rows=curr.execute('select * from dept')
# # print('--------single row------')
# # print(rows.fetchone())
# # print('--------multiple rows------')
# # print(rows.fetchmany(3))
# print('--------all rows------')
# print(rows.fetchall())
# conn.commit()
# curr.close()
# conn.close()


# =================================================
#  here we print output using loop

conn = sqlite3.connect('univ.db')
cur = conn.cursor()

rows=cur.execute('select name from dept where deptno=10 ')
allname= rows.fetchall()

for t in allname:
    print(t)

conn.commit()
cur.close()
conn.close()