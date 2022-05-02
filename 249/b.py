def has_duplicates(seq):
    return len(seq) != len(set(seq))
s = list(input())
big,small,diff = False,False,True
for x in s:
    if x.isupper(): big = True
    else: small = True
if has_duplicates(s):
    diff = False
result = "Yes" if big and small and diff else "No"
print(result)