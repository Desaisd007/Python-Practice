amount=int(input('enter the Bill Amount : '))
if amount <=1000:
    discount= (amount*10)/100
elif amount>1000 and amount<=5000:
    discount=(amount*20)/100
elif amount>5000 and amount<=10000:
   discount=(amount*30)/100
else:
    discount = (amount * 50)/100
pay= amount-discount
print ('pay amount is ',pay)