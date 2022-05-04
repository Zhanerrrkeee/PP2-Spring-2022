date = []
while True:
    s = input().split()
    if s[0] == "0":
        break
    date.append(s)
for i in range(3):
    date.sort(key = lambda y: y[i])
# date.sort(key  = lambda y: y[0])
# date.sort(key  = lambda y: y[1])
# date.sort(key  = lambda y: y[2])
for i in date:
    for j in i:
        print(j , end = " ")
    print(" ")