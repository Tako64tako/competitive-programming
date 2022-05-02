# -*- coding: utf-8 -*-
# 入力の受け取り
N=int(input())
A=list(map(int,input().split()))

# x=0,1,2,...,2000
for x in range(2001):
    # xがAに含まれないならば
    if x not in A:
        # xを出力
        print(x)
        # 終了
        exit()
