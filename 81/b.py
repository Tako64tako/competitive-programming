s = int(input())
ss = list(map(int, input().split()))

for i in range(201):
    for j in range(s):
        if ss[j] % 2 == 0:
            ss[j] /= 2
        else:
            print(i)
            exit()
