n = int(input())
s = input()

for i in range(1, n):
    for l in range(n - i + 1):
        if l + i == n or s[l] == s[l + i]:
            break
    print(l)