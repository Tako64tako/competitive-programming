from collections import Counter
from itertools import product


def solve():
    def calc(pro):
        """選び方 pro に対する答えを求める"""
        C = Counter()  # 空のカウンターを用意する
        for i in range(N):
            if pro[i]:
                # S[i]を選ぶ場合、S[i]に含まれる文字のカウントにそれぞれ1足す C.update(S[i])なら1行
                for ch in S[i]:
                    C[ch] += 1
        score = 0
        for ch, cnt in C.items():
            if cnt == K:  # K回"ちょうど"の種類数です
                score += 1
        return score

    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for pro in product((True, False), repeat=N):
        ans = max(ans, calc(pro))
    return ans


print(solve())
