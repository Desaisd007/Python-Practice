from zipfile import*


file = ZipFile('images.zip','w',ZIP_DEFLATED)
file.write('CPP.png')
file.write('Csharp.png')
file.write('java.png')
file.write('javascript.jpg')
file.write('python.png')
file.close()