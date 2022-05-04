from audioop import reverse
from re import T


date = []
while True:
    s = input().split()
    if s[0] == "0":
        break
    # s.reverse()
    date.append(reversed(s))

for i in range (3):
    date.sort(key = lambda y: y[i])
# k=3
# while k<0:
#     date.sort(key = lambda y: y[k])
# date.sort(key = lambda y : y[2])
# date.sort(key = lambda y : y[1])
# date.sort(key = lambda y : y[0])

for i in date:
    # i.reverse()
    for j in reversed(i):
        print(j , end = " ")
    print(" ")        