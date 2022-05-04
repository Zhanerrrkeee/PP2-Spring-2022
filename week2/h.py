import math
n, m  = map(int,input().split())
cor = []
t = " 0"
for i in range (int(input())):
    s = input().split()
    # s = s + t
    cor.append(s)
for i in cor:
    for j in range(1):
        i.append( math.sqrt(pow(int(i[0]) - n , 2) + pow( int ( i[1]) - m,2)))
cor.sort(key = lambda k : k[2])

for i in cor:
    for j in range(1):
        i.pop(2)


for i in cor:
    for j in i:
        print(j, end = " ")
    print(" ")

