import shutil
import os

#function of shutil module
#copy() to copy a file
shutil.copy("main.py", "main2.py")

#copytree() to copy a folder
shutil.copytree(".tutorial", "mytutorial")

#move() to move a file
shutil.move(".tutorial/file.file", "file.file")

#rmtree() to delete a folder
shutil.rmtree("mytutorial")

#os.remove() to delete a file
os.remove("file.file")