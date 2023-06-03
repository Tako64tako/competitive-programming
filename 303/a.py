N = int(input())
S = input()
T = input()

def is_similar(x, y):
    if x == y:
        return True
    if (x == '1' and y == 'l') or (x == 'l' and y == '1'):
        return True
    if (x == '0' and y == 'o') or (x == 'o' and y == '0'):
        return True
    return False

def is_similar_string(S, T):
    if len(S) != len(T):
        return False
    for i in range(len(S)):
        if not is_similar(S[i], T[i]):
            return False
    return True

if is_similar_string(S, T):
    print("Yes")
else:
    print("No")
