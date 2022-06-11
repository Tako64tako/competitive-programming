X,A,D,N = list(map(int, input().split()))

S = []
Y = X
i = 0
for _ in range(N):
    S.append(A)
    A += D
print(S)
# while True:
#     if X in S:
#         print(i)
#         break
#     if Y in S:
#         print(i)
#         break
#     X += 1
#     Y -= 1
#     i += 1