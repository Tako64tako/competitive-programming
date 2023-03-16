n,q = map(int, input().split())
yellow_cards = [[] for _ in range(n+1)]
red_cards = []
ans = []

for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        yellow_cards[x].append(1)
        if len(yellow_cards[x]) == 2:
            red_cards.append(x)
            yellow_cards[x] = []
    elif c == 2:
        red_cards.append(x)
    else:
        if x in red_cards:
            ans += ["Yes"]
        else:
            ans += ["No"]

print(*ans)