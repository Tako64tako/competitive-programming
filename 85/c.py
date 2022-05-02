N,Y = list(map(int, input().split()))

TH = 1000
FH = 5000
MH = 10000

for x in range(N+1):
    for y in range(N+1):
        z = N - x - y
        if z < 0:
            continue
        if x * TH + y * FH + z * MH == Y:
            print(z, y, x)
            exit()
print(-1, -1, -1)