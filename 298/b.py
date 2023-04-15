N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

if all(all(elem == 0 for elem in row) for row in A):
    print("Yes")
    exit()

def rotate(A):
    N = len(A)
    B = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = A[N-1-j][i]
    return B

def can_cover(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] > B[i][j]:
                return False
    return True


for _ in range(4):
    if can_cover(A, B):
        print("Yes")
        exit()
    A = rotate(A)
else:
    print("No")
