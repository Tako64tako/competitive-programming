N,A,B = list(map(int,input().split()))
h = []

for _ in range(N*A):
    for i in range(N*B):
        if abs(A-_) + abs(B-i) == 1:
            h.append("#")
        else:
            h.append(".")
    h.append("\n")
print(*h)
