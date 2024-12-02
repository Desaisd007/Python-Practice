rate=int(input('enter a salary rate per hour : '))
hour_list=[int (x) for x in input('enter day wise working hours ,separated by space  : ').split()]

total_hours=sum(hour_list)
salary=total_hours*rate

print('salary of week is : ',salary)