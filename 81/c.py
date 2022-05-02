a,b = list(map(int, input().split()))
ss = list(map(int, input().split()))

tmp = {}

for i in range(a):
    if ss[i] not in tmp:
        