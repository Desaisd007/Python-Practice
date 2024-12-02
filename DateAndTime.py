import datetime

# performing operations on date. subtraction perform on only datetime and date
d1= datetime.datetime(2022,9,27,10,10,10)
d2=datetime.datetime(2023,2,27,14,39,14)
# d3 returns days/hr/min/sec
d3=abs(d2-d1)
print(d3)
print(d1<d2)


# performing operations on time. subtraction is not work on time.
t1=datetime.time(10,10,15)
t2=datetime.time(8,5,9)
print(t1<t2)

# below we create only date object
d4=datetime.date(2015,2,6)
# below we create only time object
t4=datetime.time(10,10,10)
print(d4)
print(t4)
# combine above 2 objects and return date and time together using modulename.classname.combine()
d6=datetime.datetime.combine(d4,t4)
print(d6)




