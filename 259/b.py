import math
a, b, d = map(int, input().split())

x = a * math.cos(-math.radians(d)) - b * math.sin(-math.radians(d))
y = a * math.sin(-math.radians(d)) + b * math.cos(-math.radians(d))

print(x, y)