def pow_2(n):
    num = 0
    while(n >= num):
        yield num**2
        num += 1
gen_1  = pow_2(5)
for i in range(5):
    print(next(gen_1), end = " ")
for i in gen_1:
    print(i)
gen_2 = (x**2 for x in range(5))
print(list(gen_2))
