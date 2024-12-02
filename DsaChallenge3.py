# here we write a program for barbershop

from collections import deque

customers = deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust=customers.popleft()
    print(cust," leaved from shop")

walk_in('Ram')
walk_in('sham')
walk_in('Raj')
serviced()

print(customers)
