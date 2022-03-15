from asyncore import write
import os

print(os.path.exists("Dima.txt"))

if os.path.exists("Dima.txt"):
    f = open("Dima.txt",'r')
    print(f.read())
    with open ("Dima.txt",'a') as j:
        j.write("  KBTU ")

