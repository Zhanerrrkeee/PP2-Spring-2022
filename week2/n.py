thislist = []
while True:
	a = int(input())
	if a == 0:
		break
	thislist.append(a)
if len(thislist) % 2 == 0:	
	for i in range(int(len(thislist)/2)):
		print(thislist[i] + thislist[len(thislist)-i-1], end = " " )
else :
	thislist.insert(round(len(thislist)/2),0)
	for i in range(int(len(thislist)/2)):
		print(thislist[i] + thislist[len(thislist)-i-1], end = " " )


