import shutil
import os
import sys
from subprocess import call
curDir=os.getcwd()
print(curDir)
#os.makedirs('Test2/test3',exist_ok=True)
#os.remove('Test2')
#os.rmdir('Test2')
#os.removedir('Test2')
#os.rename('Test','Renamed')
#shutil.rmtree('Renamed',ignore_errors=True)
print(sys.platform)
#os.system("sc stop vncserver")
#call("rmdir Renamed /s /q",shell=True)
#shutil.copytree("C:\PythonPrograms", "C:\PythonPrograms2")
file = open("C:\PythonPrograms\lists.py", "r") 
lines=file.readlines()
print(lines[0].strip())
print("Amol")
print("Manthalkar")
print(lines[1].strip())
print(lines[2].strip())