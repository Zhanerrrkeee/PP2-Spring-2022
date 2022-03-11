import re

x = re.findall(".*a.*b$",input())
if x: print('Found a match')
else: print('Not matched')
