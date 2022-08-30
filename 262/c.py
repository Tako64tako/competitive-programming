N = int(input())
A = list(map(int,input().split()))
count = 0
MIN,MAX = 0,0
for i in A:
    for j in A:
        if i < j:
            MIN = i
            MAX = j
            print(MIN,MAX)
