# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc120/tasks/abc120_a
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
    a, b, c = [int(char) for char in input().split()]
    cnt = 0
    while b >= a:
        cnt += 1
        b -= a
    print(min(c, cnt))


if __name__ == '__main__':
    main()
