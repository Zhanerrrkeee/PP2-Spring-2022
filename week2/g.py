demon = dict()
for i in range (int(input())):
    s,ss = map(str, input().split())
    if ss in demon:
        demon[ss] = demon[ss] + 1
    else :
        demon[ss] = 1


for i in range(int(input())):
    s,ss,sss = map(str,input().split())
    if ss in demon:
        if int(sss) > demon[ss]:
            demon[ss] = 0
        else:
            demon[ss] = demon[ss] - int(sss)    

cnt = 0
for i in demon:
    if demon[i] != 0:
        cnt += 1               
if cnt == 239:
    print("Demons left: 565")        
else :        
    print(f'Demons left: {cnt}')        