s = input()
a = [] 
thislist = ["ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN"]
for i in s.split("+"):
	a.append(i)
firstdig = a[0]
secondig = a[1]
realdig1 = ""
realdig2 = ""
for i in range(len(secondig)):
	for j in thislist:
		if secondig[i:i+3] == j:
			realdig2 = realdig2 + str(thislist.index(secondig[i:i+3]))

for i in range(len(firstdig)):
	for j in thislist:
		if firstdig[i:i+3] == j:
			realdig1 = realdig1 + str(thislist.index(firstdig[i:i+3]))			

ans = int(realdig1) + int(realdig2)
string_ans = str(ans)

result = ""
for i in range (len(string_ans)):
	for j in range(len(thislist)):
		if string_ans[i] == str(j):
			result = result + thislist[j]

print(result)			
