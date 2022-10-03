A,B = list(map(int,input().split()))
a,b,c = False,False,False
count = 0

if A == 1:
    a = True
elif A == 2:
    b = True
elif A == 3:
    a = b = True
elif A == 4:
    c = True
elif A == 5:
    a = c = True
elif A == 6:
    b = c = True
elif A == 7:
    a = b = c = True
    
if B == 1:
    a = True
elif B == 2:
    b = True
elif B == 3:
    a = b = True
elif B == 4:
    c = True
elif B == 5:
    a = c = True
elif B == 6:
    b = c = True
elif B == 7:
    a = b = c = True



if a:
    count += 1
if b:
    count += 2
if c:
    count += 4

if count == 0:
    print(count)
    exit()
print(count)
