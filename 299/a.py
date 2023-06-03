def in_or_out(N, S):
    star_index = S.index('*')
    first_bar_index = S.index('|')
    second_bar_index = S.rindex('|')

    if first_bar_index < star_index < second_bar_index:
        return 'in'
    else:
        return 'out'


N = int(input())
S = input()

result = in_or_out(N, S)
print(result)
