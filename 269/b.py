s = []
ss = []
for _ in range(10):
    s.append(input())

i = 1
for _ in s:
    tmp = "".join(_)
    if "#" in _:
        ss.append(i)
        C = tmp.find("#") + 1
        D = tmp.rfind("#") + 1
    i += 1
A = min(ss)
B = max(ss)
print(A,B)
print(C,D)