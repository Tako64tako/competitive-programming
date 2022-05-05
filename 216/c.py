n = int(input())
pre = []
while n > 0:
    print(n)
    if n % 2 == 0:
        n = n // 2
        pre.insert(0,"B")
    else:
        n = n - 1
        pre.insert(0,"A")
print(*pre)