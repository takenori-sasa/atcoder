# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc120/tasks/abc120_b
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
    a, b, k = [int(char) for char in input().split()]
    cd = []
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            cd.append(i)

    print(cd[-k])


if __name__ == '__main__':
    main()
