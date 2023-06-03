def find_winner(N, T, cards):
    max_value = -1
    winner = -1

    target_color_found = any(card[0] == T for card in cards)

    for i, (color, value) in enumerate(cards):
        if (target_color_found and color == T) or (not target_color_found and color == cards[0][0]):
            if value > max_value:
                max_value = value
                winner = i + 1

    return winner


N, T = map(int, input().split())
colors = list(map(int, input().split()))
values = list(map(int, input().split()))

cards = [(colors[i], values[i]) for i in range(N)]

print(find_winner(N, T, cards))
