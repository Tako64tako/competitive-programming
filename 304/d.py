W, H = map(int, input().split())
N = int(input())

strawberries = []
for _ in range(N):
    p, q = map(int, input().split())
    strawberries.append((p, q))

A, B = map(int, input().split())

cake = [[False] * H for _ in range(W)]
for strawberry in strawberries:
    p, q = strawberry
    cake[p][q] = True

min_strawberries = float('inf')
max_strawberries = 0

for a in range(1, A+1):
    for b in range(1, B+1):
        piece_strawberries = 0
        for i in range(a):
            for j in range(b):
                if cake[i][j]:
                    piece_strawberries += 1
        min_strawberries = min(min_strawberries, piece_strawberries)
        max_strawberries = max(max_strawberries, piece_strawberries)

print(min_strawberries, max_strawberries)
