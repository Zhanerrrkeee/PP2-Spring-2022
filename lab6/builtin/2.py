cnt = [0,0]
for i in input():
    if i.islower():
        cnt[0] += 1
    elif i.isupper():
        cnt[1] += 1


print(f'upper case - {cnt[1]} , lower case - {cnt[0]}')            
        
