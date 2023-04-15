H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 操作回数の最大値は W * H であり、
# この数だけ操作を繰り返すことで全ての '.' を 'PCT' にできる。
for _ in range(W * H):
    updated = False
    for i in range(H):
        for j in range(W - 1):
            if S[i][j] == 'T' and S[i][j+1] == 'T':
                S[i] = S[i][:j] + 'PCT' + S[i][j+3:]
                updated = True
    if not updated:
        break

# 出力する
for s in S:
    print(s)
