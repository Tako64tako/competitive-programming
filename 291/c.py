n = int(input())
s = input()

x, y = 0, 0
pos_set = {(0, 0)}
for c in s:
    if c == "R":
        x += 1
    elif c == "L":
        x -= 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1

    pos = (x, y)
    if pos in pos_set:
        print("Yes")
        exit()
    pos_set.add(pos)

print("No")