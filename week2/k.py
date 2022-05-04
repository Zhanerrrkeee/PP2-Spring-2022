s = input()
a = []
s1 = s2 = s3 = s4 = ""

for i in s.split("!"):
	s1 = s1 + i	
for i in s1.split("?"):
	s2 = s2 + i
for i in s2.split(","):
	s3 = s3 + i
for i in s3.split():
	a.append(i)
a.sort()
res = []
for i in a:
	if i not in res:
		res.append(i)


print(len(res))
for i in res:
	print(i)	

	