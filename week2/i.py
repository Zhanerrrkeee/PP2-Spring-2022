inl = []
outl = []

for i in range (int(input())):
    s = input().split()
    if s[0] == "1" :
        inl.append(s[1])
    elif s[0] == "2" :
        outl.append(inl[0])
        inl.remove(inl[0])

for i in outl:
    print(i , end = " ")