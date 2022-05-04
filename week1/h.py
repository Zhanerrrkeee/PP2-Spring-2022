x = input()
a = input()
arr = []
for i in range(len(x)):
	if(x[i]==a):
		arr.append(i)
# print (len(arr))		
if(len(arr)>2):
    print(arr[0], end = " ")
    print(arr[len(arr)-1])
else:
    for i in range(len(arr)):
        print(arr[i], end = " ")
