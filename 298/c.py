def bisect_left(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

N = int(input())
Q = int(input())
cards = [[] for _ in range(N)]  # 箱の中身を格納する配列
nums = [[] for _ in range(2 * 10**5)]  # カードの入っている箱の番号を格納する配列

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        lo = bisect_left(cards[j-1], i)
        cards[j-1].insert(lo, i)
        if not j in nums[i-1]:
            lo = bisect_left(nums[i-1], j)
            nums[i-1].insert(lo, j)
    elif query[0] == 2:
        i = query[1]
        print(*cards[i-1])
    else:
        i = query[1]
        print(*nums[i-1])
