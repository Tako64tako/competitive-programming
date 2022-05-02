n = int(input())
a  = list(map(int,input().split()))
x = int(input())
i,k = 0,0

while x > i:
    for b in a:
        i += b
        k+=1
print(k-1)
