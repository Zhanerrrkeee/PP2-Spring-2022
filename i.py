mail = "@gmail.com"
for i in range(int(input())):
    s = str(input())
    k=s.find(mail,0,len(s))
    if k == len(s)-10 and len(s)>10:
        print(s[0 : k])