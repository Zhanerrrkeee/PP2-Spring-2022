date = []
while True:
    s = input().split()
    if s[0] == "0":
        break
    s.reverse()
    date.append(s)
    
date.sort()
for i in date:
    i.reverse()
    for j in i:
        print(j, end = " ")
    print(" ")    