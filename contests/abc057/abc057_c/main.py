# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc057/tasks/abc057_c
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
    max_l = len(str(10**10))
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            max_l = min(max_l, max(len(str(i)), len(str(n//i))))
    print(max_l)


if __name__ == '__main__':
    main()
