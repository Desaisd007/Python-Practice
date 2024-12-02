# in os module having lot of functions related to operating system functionality,
import os

# os.name is return device operating sytem name
print(os.name)
print(os.getlogin())

# os.getcwd() it return current working directory
print(os.getcwd())

# os.chdir() - its used to change working directory

# os.listdir() - shows the all files in current directory
print(os.listdir())

# os.mkdir() it create new directory(folder)

# os.remove("mention here file path")  that function is delete file only
# os.rmdir('mention dir path here') that fuction remove  directory.
# os.removedirs()that function remove all directories

# os.rename('enter current name of folder','enter new for folder') remember that function not work on cwd.