X,Y,Z = list(map(int,input().split()))

def print_set(a):
    print(a)
    exit()

if X > 0:
    if Y > X:
        print_set(abs(X))
    elif Y < 0:
        print_set(abs(X))
    elif X > Y > Z > 0:
        print_set(abs(X))
    elif Z < 0:
        Z = abs(Z) * 2
        print_set(X + Z)
    else:
        print(-1)
        exit()
else:
    if Y < X:
        print_set(abs(X))
    elif Y > 0:
        print_set(abs(X))
    elif X < Y < Z < 0:
        print_set(abs(X))
    elif Z > 0:
        Z = -Z * 2
        print_set(abs(X + Z))
    else:
        print(-1)
        exit()