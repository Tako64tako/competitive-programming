N = int(input())
S = input()

good_count = 0
bad_count = 0
for i in range(N):
    if S[i] == 'o':
        good_count += 1
    elif S[i] == 'x':
        bad_count += 1

if good_count > 0 and bad_count == 0:
    print("Yes")
else:
    print("No")
