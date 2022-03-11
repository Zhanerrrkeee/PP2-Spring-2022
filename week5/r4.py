import re
 
x = re.findall(".*[A-Z][a-z].*", input())
if x: print("Found a match")
else: print("Not matched")
