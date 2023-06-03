from collections import defaultdict


def solve(N, M, a):
    edge = defaultdict(set)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                edge[i].add(j)

    for i in range(M):
        for j in range(N-1):
            if a[i][j+1] in edge[a[i][j]]:
                edge[a[i][j]].remove(a[i][j+1])
            if a[i][j] in edge[a[i][j+1]]:
                edge[a[i][j+1]].remove(a[i][j])

    cnt = 0
    for k in edge:
        cnt += len(edge[k])
    return cnt // 2


N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
print(solve(N, M, a))
