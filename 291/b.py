N = int(input())
S = list(map(int,input().split()))

for i in range(N):
    S.remove(max(S))
    S.remove(min(S))

print(sum(S)/len(S))