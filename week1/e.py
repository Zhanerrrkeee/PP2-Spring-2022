import math

def ItIsPrime(n):
	if n == 1 or n == 2 or n == 3: return True
	for i in range (2,n):
		if n % i == 0:
			return False
	return True		

a,b = map (int, input().split())
if ItIsPrime(a) == True and b % 2 == 0 and a<500:
	print("Good job!")
else:
    print ("Try next time!")	
