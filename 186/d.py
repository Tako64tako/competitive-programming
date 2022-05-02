s = int(input())
ss = list(map(int,input().split()))
a = 0
for i in range(s-1):
    for j in range(len(ss)):
        a += abs(ss[i] - ss[j])
        print(a)
print(a)