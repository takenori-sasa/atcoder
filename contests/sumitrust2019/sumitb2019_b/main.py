# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
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
    for i in range(1, n+1):
        if int(i*1.08) == n:
            print(i)
            return
    print(':(')


if __name__ == '__main__':
    main()
