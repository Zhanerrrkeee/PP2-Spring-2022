
import os

WORKING_DIR = os.getcwd()
def fun3():
  for i in os.listdir(WORKING_DIR):
    targetPath = os.path.join(WORKING_DIR,i)
    if os.path.isdir(targetPath):
      print(f'DIR: {i}')

def fun2():
  for i in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR,i)
    if os.path.isfile(target_path):
      print(f'FILE: {i}')

def fun1():
  for i in os.listdir(WORKING_DIR):
    print(i)    

print("If u want to see files and dir type 1,if only files 2,if only dir 3")
a = int(input()) 
if a == 1:
  fun1()
elif a == 2:
  fun2()
elif a ==3:
  fun3()       
      
          
          