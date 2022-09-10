# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
from itertools import permutations, combinations
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc128/tasks/abc128_c
    for _ in range(n):
        a = [int(char) for char in input().split()]
    data = [input().split() for _ in range(n)]
    print(*ans, sep="\n")
転置
    trans=map(list, zip(*data))
'''
# INF = float('inf')
# MOD = 10**9+7


def main():
    n, m = [int(char) for char in input().split()]
    lump = []
    for _ in range(m):
        s = [int(char)-1 for char in input().split()]
        lump.append(set(s[1:]))
    p = [int(char) for char in input().split()]
    # print(*lump, sep="\n")
    cnt = 0
    for i in range(n+1):
        for comb in combinations(range(n), i):
            # print('start', comb)
            is_on = True
            for j in range(m):
                num_on = 0
                for lu in lump[j]:
                    if lu in comb:
                        num_on += 1
                if num_on % 2 != p[j]:
                    is_on = False
            if is_on:
                # print('cnt', comb)
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
