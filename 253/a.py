N = list(map(int, input().split()))
S = sorted(N)
result = "Yes" if N[1] == S[1] else "No"
print(result)