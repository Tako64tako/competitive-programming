s = list(map(int, input().split()))
# print(s[0],s[1],s[2])
i = 0
while True:
    if s[0] >= s[1]:
        print(i)
        exit()
    elif s[1] > s[0]:
        s[0] *= s[2]
        i += 1
