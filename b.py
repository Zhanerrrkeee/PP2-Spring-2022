s = str(input())
sum1 = 0 
for i in s:
	sum1 = sum1 + ord(i)

if (sum1>300):
    print ("It is tasty!")	
else:
    print ("Oh, no!")