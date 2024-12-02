# He we complete shop challenge where we have 3 tables order/customer/product .
# product and customer are connected to order

import mysql.connector

# Connect to MySQL without specifying a database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='satyajeet'
)

cur = conn.cursor()

# Create the database
cur.execute("CREATE DATABASE IF NOT EXISTS shop")

# Close the connection to the database
cur.close()
conn.close()

# Now connect to the newly created database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='shop'
)

cur = conn.cursor()

# Create customer table first
cur.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    Customer_id INT AUTO_INCREMENT PRIMARY KEY,
    Cname VARCHAR(255),
    Address VARCHAR(255)
);
''')

# Create product table second
cur.execute('''
CREATE TABLE IF NOT EXISTS Product (
    Product_no INT AUTO_INCREMENT PRIMARY KEY,
    pname VARCHAR(255),
    price DECIMAL(10, 2)
);
''')

# Create order table third
cur.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_No INT AUTO_INCREMENT PRIMARY KEY,
    Customer_id INT,
    Product_no INT,
    Qty INT,
    FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
    FOREIGN KEY (Product_no) REFERENCES Product(Product_no)
);
''')

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()


