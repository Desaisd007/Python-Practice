# we write program for inventory
from collections import Counter
inventory=Counter(Apple= 50,Banana= 30,Orange=20,Mango=100)

def update_inventory(order):
    inventory.subtract(order)

order=Counter(Apple= 30,Banana= 15,Orange=5,Mango=60)
update_inventory(order)
print(inventory)