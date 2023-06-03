def max_dango_level(S):
    N = len(S)
    max_level = 0

    for i in range(N):
        for j in range(i+1, N+1):
            sub_string = S[i:j]
            if sub_string[0] == '-' and sub_string[-1] == 'o' or sub_string[0] == 'o' and sub_string[-1] == '-':
                if sub_string.count('o') == len(sub_string) - 1:
                    level = len(sub_string) - 1
                    max_level = max(max_level, level)

    return max_level if max_level > 0 else -1

N = int(input())
S = input()
print(max_dango_level(S))
