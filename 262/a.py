S = int(input())

if S % 4 == 2:
    print(S)
else:
    while S % 4 != 2:
        S += 1
    print(S)