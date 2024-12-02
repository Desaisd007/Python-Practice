# Os path is define that the given path pr file are avail or not
import os
# os.path.exists() defines path is true or false. we want to enter path here
# os.path.isfile() enter path of file . they return true or false
# os.path.isdir()  enter path of directory(folder) .function return true or false

# os.path.split()- it split file and remaining part
print(os.path.split('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython'))

# os.path.join()- it joins the path
print(os.path.join('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject', 'MyPython'))

# basename() - it shows filename only
print(os.path.basename('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython\\CPP.png'))

# dirname()- it shows directory name
print(os.path.dirname('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython\\CPP.png'))

# os.path.getmtime()  is show modified time of path or file. but it return epoch time. we want real time then we want to import time module
print(os.path.getmtime(('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython')))
import time
print(time.ctime(os.path.getmtime('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython')))

# os.path.getctime()  is show creation time of path or file. but it return epoch time. we want real time then we want to import time module
print(os.path.getctime(('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython')))
import time
print(time.ctime(os.path.getctime('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython')))


# os.path.relpath() - it compress the path (show only folder and file name)
print(os.path.relpath('C:\\Users\\satya\\PycharmProjects\\First\\pythonProject\\MyPython\\CPP.png'))

# os.path.abspath() - it return full(absolute) path on the bases of relational path
print(os.path.abspath('..\\MyPython\\CPP.png'))