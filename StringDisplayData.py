item=input('enter the name of item : ')
price=input('enter the price :')

total_length=len(item)+len(price)
dots='.'* (25-total_length)
print(item+dots+price)