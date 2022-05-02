N = int(input())
S = []
for n in range(1, N+1):
    S = S+[n]+S
print(*S)