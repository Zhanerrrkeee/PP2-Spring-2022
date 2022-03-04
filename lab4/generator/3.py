from re import I


def div_34(n):
    i = 0
    while i <= n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
            i += 1
        else:
            i += 1 


gen_34 = div_34(int(input()))
for i in gen_34:
    print(i , end = " ")                