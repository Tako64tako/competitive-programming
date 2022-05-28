N = int(input())
s = []
t = []
for _ in range(N):
    S,T = list(input().split())
    s.append(S)
    t.append(T)
p = sorted(t)
print(set(s))