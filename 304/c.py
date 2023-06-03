from scipy.spatial import KDTree
from collections import deque

N, D = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

tree = KDTree(points)

infected = [False] * N
infected[0] = True

queue = deque([points[0]])

# Process the queue
while queue:
    point = queue.popleft()
    idx_point = points.index(point)

    # Get the points within distance D
    ind = tree.query_ball_point(point, D)
    
    # Check if any of these points are not yet infected
    for i in ind:
        if not infected[i]:
            infected[i] = True
            queue.append(points[i])

# Print the results
for inf in infected:
    print('Yes' if inf else 'No')
