N,M,X,T,D = list(map(int,input().split()))
a = N - X
if a > X:
    print(T)
else:
    print((T - D) * (M - X) + D * a)
    #((N-X)-M)*D
