# here we learn datetime to string and string to datetime
import datetime
from datetime import *

d1=datetime(2014,12,6,15,25,10)
print(d1)

# for transfer datetime to str use (strftime)
d2=d1.strftime('%d-%b-%y %a %H:%M:%S')
print(d2)
print(type(d2))

# for transfer str to datetime use (strptime)
d3=datetime.strptime(d2,'%d-%b-%y %a %H:%M:%S')
print(d3)
print(type(d3))

str1='10/08/2023 14:30:15 Sun'
d4=datetime.strptime(str1,'%m/%d/%Y %H:%M:%S %a')
print(d4)