# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc128/tasks/abc128_b
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
    n = int(input())
    rest = {}
    for i in range(n):
        s, c = [char for char in input().split()]
        p = int(c)
        if s not in rest:
            rest[s] = {}
        rest[s][p] = i+1
    n_reco = 1
    for city in sorted(rest.keys()):
        for i in range(100, -3, -1):
            if i in rest[city]:
                print(rest[city][i])


if __name__ == '__main__':
    main()
