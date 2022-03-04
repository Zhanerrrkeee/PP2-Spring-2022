from operator import ge


def func(n):
    i = 0
    while(i < n):
        if i % 2 == 0:
            yield i
            i += 1  
        else:
            i += 1     

gen_even_numbres = func(int(input()))
for i in gen_even_numbres:
    print(i , end  = " ") 
    
    
# gen_2 = (x*2 for x in range(int(int(input())/2)))
# print(list(gen_2))                  