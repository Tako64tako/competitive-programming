S = input()

for i in range(len(S)):
    if S[i].isupper():
        A = i
        print(A+1)