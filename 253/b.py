H,W = list(map(int, input().split()))
R = [input() for _ in range(H)]
i = 0
S,SS = list(),list()
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

for _ in R:
    S.append(my_index(_, 'o', default=False))
    if type(S) == int:
        SS.append(i)
    i += 1
    
# abs(SS[0] - S[0]) + abs(SS[1] - S[1])
print(SS[0],S[0])
