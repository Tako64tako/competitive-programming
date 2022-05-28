Q = int(input())
SS = list()
R = list()
flg = False
for _ in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        SS.append(S[1])
    elif S[0] == 2:
        for i in range(S[2]):
            if SS.count(S[1]) == 0:
                break
            else:
                SS.remove(S[1])
    else:
        R.append(max(SS) - min(SS))
        flg = True
if flg:
    for _ in R:
        print(_)