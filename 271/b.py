N,Q = map(int,input().split())

a = [0] * N
s = [0] * Q
t = [0] * Q

for _ in range(N):
    a[_] = list(map(int,input().split()))
    # print(a[_])
for _ in range(Q):
    s[_],t[_] = map(int,input().split())
    # print(f's[_]={s[_]},t[_]={t[_]}')

for _ in range(Q):
    print(a[s[_]-1][t[_]])