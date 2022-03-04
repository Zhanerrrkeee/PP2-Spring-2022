from operator import ge

def nums(n):
    while n >= 0:
        yield n
        n=n-1

gen1 = nums(int(input()))
print(list(gen1))
             
        