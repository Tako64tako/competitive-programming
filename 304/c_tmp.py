class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (self.x - self.w <= point.x <= self.x + self.w) and (self.y - self.h <= point.y <= self.y + self.h)

    def intersects(self, range):
        return not (range.x - range.w > self.x + self.w or range.x + range.w < self.x - self.w or
                    range.y - range.h > self.y + self.h or range.y + range.h < self.y - self.h)

class QuadTree:
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def insert(self, p):
        if not self.boundary.contains(p):
            return False

        if len(self.points) < self.capacity:
            self.points.append(p)
            return True
        else:
            if not self.divided:
                self.subdivide()

            return (self.northeast.insert(p) or
                    self.northwest.insert(p) or
                    self.southeast.insert(p) or
                    self.southwest.insert(p))

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w / 2
        h = self.boundary.h / 2

        ne = Rectangle(x + w, y - h, w, h)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - w, y - h, w, h)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w, y + h, w, h)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - w, y + h, w, h)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def query_range(self, range):
        found = []

        if not self.boundary.intersects(range):
            return found

        for p in self.points:
            if range.contains(p):
                found.append(p)

        if self.divided:
            found.extend(self.northeast.query_range(range))
            found.extend(self.northwest.query_range(range))
            found.extend(self.southeast.query_range(range))
            found.extend(self.southwest.query_range(range))

        return found

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root

N, D = map(int, input().split())
points = [Point(*map(int, input().split()), i) for i in range(N)]

# Create a boundary that sufficiently covers all points.
# This could be improved by using the min and max of the actual data.
boundary = Rectangle(0, 0, 1e9, 1e9)
qt = QuadTree(boundary, 4)  # QuadTree with capacity 4

for point in points:
    qt.insert(point)

uf = UnionFind(N)

# Searching for clusters
for point in points:
    query_range = Rectangle(point.x, point.y, D, D)
    points_in_range = qt.query_range(query_range)
    for point_in_range in points_in_range:
        if ((point.x - point_in_range.x)**2 + (point.y - point_in_range.y)**2) <= D**2:
            uf.union(point.id, point_in_range.id)

infected_root = uf.find(0)

for i in range(N):
    print('Yes' if uf.find(i) == infected_root else 'No')
