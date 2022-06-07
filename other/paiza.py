S = list(map(int, input().split()))

kame = max(S[0],S[1])
turu = max(S[2], S[3])
drlta = kame - turu
turu_num = (S[1]*kame-S[0])//drlta
kame_num = S[1] - turu_num

print(turu_num,kame_num)

