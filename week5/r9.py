import re
s = input()
t = ''
for i in range(len(s)):
    if s[i].isupper():
        t += '_'
        t += s[i]
    else:
        t += s[i]
g = re.split(r'_',t)
for i in g:
    print(i, end=" ") 