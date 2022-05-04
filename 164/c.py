import collections
S = int(input())
SS = [input() for _ in range(S)]
j = 0
c = collections.Counter(SS)
for i in c:
    j+=1
print(j)