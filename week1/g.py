import math
x =  input ()
sum1 = 0
ans = len(x)-1
for i in x:
	if i == "1":
		sum1+= pow(2,ans)
		ans = ans - 1
	else :
	    ans = ans - 1	

print (int(sum1))
