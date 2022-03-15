import os

l = [str(x**2) for x in range(10)]
x = ' '.join(l)
f = open('Dima.txt','a')
f.write('\n'+x)

with open('Dima.txt','r') as f:
    s = f.read()
    
print(s)    