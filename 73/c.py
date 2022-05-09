from curses import A_BOLD


N = int(input())
A = set()
for _ in range(N):
    s = int(input())
    if s in A:
        A.remove(s)
    else:
        A.add(s)
print(len(A))