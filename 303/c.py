N, M, H, K = map(int, input().split())
S = input().strip()
items = {tuple(map(int, input().split())) for _ in range(M)}

x, y = 0, 0
for direction in S:
    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1

    H -= 1
    if H < 0:
        print('No')
        break
    if (x, y) in items and H < K:
        H = K
else:
    print('Yes')
