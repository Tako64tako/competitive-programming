R,C= list(map(int, input().split()))
A11, A12 = list(map(int, input().split()))
A21, A22 = list(map(int, input().split()))

if R==1 and C==1:
    print(A11)
elif R==1 and C==2:
    print(A12)
elif R==2 and C==1:
    print(A21)
elif R==2 and C==2:
    print(A22)
