S = list(input())
ary = [False] * 10
for count, _ in enumerate(S):
    if int(_) == 0:
        ary[count] = True
    if ary[0] == True:
        pass
    else:
        print("No")
        exit()

if ary[0] == True:
    if ary[2] and ary[8] == True:
        if (ary[5] or ary[9] == False) and (ary[3] or ary[4] or ary[6] or ary[7] == False):
            print("Yes")
        else:
            print("No")
    elif ary[1] and ary[7] == True:
        if (ary[3] or ary[6] == False) and (ary[4] or ary[5] or ary[8] or ary[9] == False):
            print("Yes")
        else:
            print("No")
    elif ary[3] == True:
        if ary[6] == False and (ary[1] or ary[2] or ary[4] or ary[5] or ary[7] or ary [8] or ary[9] == False):
            print("Yes")
        else:
            print("No")
    elif ary[5] == True:
        if ary[9] == False and (ary[1] or ary[2] or ary[3] or ary[4] or ary[6] or ary [7] or ary[8] == False):
            print("Yes")
        else:
            print("No")
    elif ary[4] == True:
        if (ary[1] or ary[3] or ary[6] or ary[7] == False) and (ary[2] or ary[5] or ary[8] or ary[9] == False):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
