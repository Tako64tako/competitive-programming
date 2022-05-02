s = list(map(int,input()))
for ss in range(len(s)+1):
    if ss not in s:
        print(ss)
        exit()