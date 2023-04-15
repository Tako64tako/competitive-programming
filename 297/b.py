s = input()

# 条件1のチェック
if set(s) != set('KQRBN') or s.count('K') != 1 or s.count('Q') != 1 or s.count('R') != 2 or s.count('B') != 2 or s.count('N') != 2:
    print('No')
else:
    # 条件2のチェック
    b_indices = [i for i in range(8) if s[i] == 'B']
    if any(i % 2 == j % 2 for i, j in zip(b_indices, b_indices[1:])):
        print('No')
    else:
        # 条件3のチェック
        r_indices = [i for i in range(8) if s[i] == 'R']
        k_index = s.index('K')
        if not any(i < k_index < j for i, j in zip(r_indices, r_indices[1:])):
            print('No')
        else:
            print('Yes')
