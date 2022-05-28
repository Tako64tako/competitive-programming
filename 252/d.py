import itertools
N = int(input())
A = list(map(int, input().split()))
A = sorted(set(A),key=A.index)
comb = itertools.combinations(A, 3)
print(len(list(comb)))
