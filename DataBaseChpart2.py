import mysql

conn=mysql.connector.connect('Customer.db')
curr=conn.cursor()

curr.execute('insert into Customer values(C101,Ram,delhi)')
conn.commit()
curr.close()
conn.close()


