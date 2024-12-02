# Here we writting program for bills and subtotals
from collections import Counter
prices = {"soap": 25,"toothpaste": 30,"shampoo": 5,"toothbrush": 20}

print(f'{"product":13} {"Price":6} {"Qty":6} {"Amount":5}')
def generated_bill(order):
    total=0
    for item,qty in order.items():
        print(f'{item:15}{prices[item]:3}  X {qty:3} = {prices[item]* qty:5}')
        total+=prices[item]* qty

    print('Total Amount of purchase :',total)

order=Counter(soap=3,toothpaste=2,shampoo=1,toothbrush=4)
generated_bill(order)