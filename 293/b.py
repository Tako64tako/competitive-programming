# coding: utf-8
# Your code here!
N = int(input())
A = input().split()
flag = []
for i in range(N):
    flag.append(1)

for i in range(N):
    if flag[i] == 1:
        flag[int(A[i])-1] = 0

K = 0
for i in range(N):
    K += flag[i]

print(K)
for i in range(N):
    if(flag[i] == 1):
        print(i+1, end=' ')
