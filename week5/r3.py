import re
x = re.findall(".*_[a-z].*|.*[a-z]_.*",input())
if x: print("Found a match")
else: print("Not matched")
