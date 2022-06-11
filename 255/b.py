import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(N)]
tmp = 99999
R = 0
for _ in range(N):
    if _+1 not in A:
        tmp = 999999
        for i in A:
            r = np.linalg.norm(np.array(l[i-1]) - np.array(l[_]))
            if r < tmp:
                tmp = r
        if R < tmp:
            R = tmp
print(R)
