n = int(input())
k = input()
if k == 'k':
    m = input()
    ansformat = "{:." + m +"f}"
    print(ansformat.format(n/1024))
elif k == 'b':
    print(n*1024)
