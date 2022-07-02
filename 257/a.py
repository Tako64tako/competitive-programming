N,C = list(map(int,input().split()))
S = ''
for _ in range(26):
    S += chr(ord("A") + _) * N
print(S[C-1])