H,W = list(map(int,input().split()))
X = [0] * H
a = []
for _ in range(H):
    X[_] = input()
    for i in range(W):
        if X[_][i] == "#":
            a += [i]
for _ in range(W):
    print(a.count(_),end=' ')