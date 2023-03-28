# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc106/tasks/abc106_b
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
    cnt = 0
    for i in range(1, n+1, 2):
        d = 0
        for j in range(1, i+1, 2):
            if i % j == 0:
                d += 1
        if d == 8:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
