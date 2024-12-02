roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

number= input('enter roman number in upper cases : ')
number2=number.upper()

deci_num=0
i=0
while i<len(number2):
    if i+1<len(number2) and roman[number2[i]]<roman[number2[i+1]]:
        deci_num+=roman[number2[i+1]]-roman[number2[i]]
        i+=2
    else:
        deci_num+=roman[number2[i]]
        i+=1

print(deci_num)