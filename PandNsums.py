num_of_nums=int(input('enter the rotation number :'))

psum,nsum,count=0,0,0
while count<num_of_nums:
   n=int(input('enter a numbers :'))
   if n>0:
       psum+=n
   else:
       nsum+=n

   count+=1

print( 'positive sum =',psum)
print( 'negative sum =',nsum)