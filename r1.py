import re
# f = open('row.txt','r')
# temp = f.read()
x = re.search('.*a(b*).*', input("Write something: "))
if x: print("Found a match")
else: print("Not matched")    
# print(x)