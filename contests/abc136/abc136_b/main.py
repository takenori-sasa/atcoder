# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc136/tasks/abc136_b
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
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
