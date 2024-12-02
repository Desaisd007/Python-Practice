
with open('my.data','rb') as f:
  # print(f.read(2)  here print 1st two letter with prefix 'b' because its encoded file
# -----------------------------------
  # print(f.read(2).decode()) use decode() to avoid prefix in output
# -----------------------------------
  # here we use seek for random access binary file
  # print(f.read(2).decode())
  # # upper statement print 'ab' and lower seek will count
  # # next 3 element from that b because we use 1(start pn last stop)
  # f.seek(3,1)
  # # below print will print 2 values
  # print(f.read(2).decode())
# -------------------------------------
#  now we print bits from back
 print(f.read(2).decode())
 f.seek(-3,2)
 print(f.read(3).decode())
 #-------------------------------------
 # tell is told us file pointers current index
 print(f.tell())
