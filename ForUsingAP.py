initial=int(input('enter a initial term : '))
diff=int(input('enter a difference : '))
number=int(input('enter number of terms :'))

for i in range(initial,initial+diff*number,diff):
    print(i)