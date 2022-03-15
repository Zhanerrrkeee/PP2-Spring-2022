import os

with open('Dima.txt','r') as f:
    text = f.read()

wr = open('copy.json','w')
wr.write(text)

    