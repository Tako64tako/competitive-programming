import itertools
list = list(map(int, input().split()))
i,j = 0,0
box = [i],[j]
for _ in list:
    all = itertools.product(range(1,_), repeat=3)
    for x in all:
        if sum(x) == _:
            box[i][j] = x
            print(box[i][j])
        j += 1
    i += 1

