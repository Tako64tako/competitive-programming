s = int(input())
ss = list(map(int, input().split()))
maxnum,result = 0,0
for i in range(s):
    maxnum = max(maxnum, ss[i])
    result += maxnum - ss[i]
print(result)