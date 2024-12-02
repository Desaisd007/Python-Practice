sentence=input('enter sentence : ')

print(sentence)
d={}
for i in sentence:
    if i != ' ':
      count = sentence.count(i)
      if i not in d:
        d[i]= count

print (d)


