n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
count = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1  # 有向グラフなら消す
# print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]


graph_new = []
for i in range(n):
    tmp_l = []
    for j in range(n):
        # print("---------")
        # print(graph[i][j])
        # print(graph[i-1][j-1])
        if graph[i][j] > 0:
            tmp_l.append(j)
            if tmp_l == tmp_l[::-1]:
                count += 1
    graph_new.append(tmp_l)
    #count += 1
# print(graph_new)
print(count)
