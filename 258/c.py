N,Q = list(map(int,input().split()))
S = input()
num = 0
for _ in range(Q):
    t,x = list(map(int,input().split()))
    if t == 1:
        num += x
    else:
        print(S[(x-num-1)%N])