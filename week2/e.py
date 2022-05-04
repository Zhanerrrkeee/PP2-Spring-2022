arr = []
las = []
n = input()
if " " not in n:
    x = int(input())
else :
    for i in n.split():
        las.append(i)
    n = int(las[0])
    x = int(las[1])
for i in range (int(n)):
    arr.append(x + 2 * i)
result = arr[0]
for i in range(1 , len(arr)):
    result = result ^ arr[i]
print(result)