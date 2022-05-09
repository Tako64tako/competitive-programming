N,Q =list(map(int,input().split()))
S = list(range(1,N+1))

for _ in range(1,N+1):
    X = int(input())
    if S == X:
        print("hoge")
        S.insert(_,_+1)
print(S)