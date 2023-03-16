H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def dfs(i, j, seen):
    if i == H-1 and j == W-1:
        return 1
    res = 0
    if j < W-1 and A[i][j+1] not in seen:
        seen.add(A[i][j+1])
        res += dfs(i, j+1, seen)
        seen.remove(A[i][j+1])
    if i < H-1 and A[i+1][j] not in seen:
        seen.add(A[i+1][j])
        res += dfs(i+1, j, seen)
        seen.remove(A[i+1][j])
    return res

seen = set([A[0][0]])
print(dfs(0, 0, seen))
