N = int(input())
A = list(map(int, input().split()))
i,box,P = 0,0,0
first,second,third,home = False,False,False,False
for _ in A:
    # print(_)
    home = True
    if third:
        P += 1
        third = False
    if second:
        if _ >= 2:
            P+=1
            second = False
        if _ == 1:
            third = True
            second = False
    if first:
        if _ >= 3:
            P+=1
            first = False
        if _ == 2:
            third = True
            first = False
        if _ == 1:
            second = True
            first = False
    if home:
        # print("hoge")
        if _ >= 4:
            P += 1
            home = False
        if _ == 3:
            third = True
            home = False
        if _ == 2:
            second = True
            home = False
        if _ == 1:
            first = True
            home = False
    # print(home,first,second,third)
print(P)