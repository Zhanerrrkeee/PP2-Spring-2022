import os
from re import L
l = [chr(i+65)+'.txt' for i in range(26)]
for i in l:
    f = open(i,'w')
    
