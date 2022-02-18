a = list(map(int,input().split()))
def filter_prime(n):
	if n == 1 or n == 2 or n == 3: return True
	for i in range (2,n):
		if n % i == 0:
			return False
	return True	
for i in a:
    if filter_prime(i):
        print(i, end = " ")
        
           