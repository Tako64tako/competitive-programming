N = int(input())
A =  list(map(int,input().split()))
odd1 = 0
odd2 = 0
even1 = 0
even2 = 0

for _ in A:
    if _ % 2 == 1:
        if odd1 < _:
            odd2 = odd1
            odd1 = _
        elif odd2 < _:
            odd2 = _
    else:
        if even1 < _:
            even2 = even1
            even1 = _
        elif even2 < _:
            even2 = _

if odd2 == 0 and even2 == 0:
    print(-1)
else:
    if (odd1 + odd2) > (even1 + even2):
        print(odd1+odd2)
    else:
        print(even1+even2)