f=open('python1.png','rb')
data= f.read()

cp=open('python2.png','wb')
cp.write(data)

f.close()
cp.close()
