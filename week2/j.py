def CheckIsItNumber(n):
	cntu = 0
	cntl = 0
	cntn = 0
	for i in range(len(n)):
		if 48 <= ord(n[i]) <= 57:	
			cntn = cntn + 1
		elif 65 <= ord(n[i]) <= 90:
			cntu = cntu + 1  
		elif 97 <= ord(n[i]) <= 122:
			cntl = cntl + 1
	if cntl >= 1 and cntu >= 1 and cntn >= 1:
		return True
	return False			


a = []

for i in range(int(input())):
	s = input()
	if CheckIsItNumber(s):
		a.append(s)

n = []
for i in a:
	if i not in n:
		n.append(i)

n.sort()
print (len(n))
for i in n:
	print(i)
