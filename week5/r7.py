import re

x = re.split("_",input())
print(x[0],end="")
for i in range(1,len(x)):
    print(x[i].capitalize(), end = "" )
    