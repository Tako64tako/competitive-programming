H,W = list(map(int,input().split()))
R,C = list(map(int,input().split()))
p = 0
for _ in range(1,H+1):
    for i in range(1,W+1):
        if abs(R-_) + abs(C-i) == 1:
            p += 1
print(p)