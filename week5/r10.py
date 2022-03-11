import re
s = input()
t = ''
for i in range(len(s)):
    if s[i].isupper():
        t  += " "
        t  += s[i]
    else: t += s[i]

z = re.sub('\s','_',t)
for i in z:
    print(i.casefold(),end="")
        
