s = input()
ss = sorted(list(map(int, input().split())), reverse=True)
a,b,flg=0,0,True
for i in ss:
    if flg:
        a += i
        flg = False
    else:
        b += i
        flg = True
print(a-b)