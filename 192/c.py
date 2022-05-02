c,j = list(input().split())
d = 0
for i in range(int(j)):
    a = (''.join(sorted(c)[::-1]))
    b = (''.join(sorted(c)))
    c = int(a) - int(b)
    if c == d:
        exit()
    c = str(c)
    d = str(c)
print(c)

