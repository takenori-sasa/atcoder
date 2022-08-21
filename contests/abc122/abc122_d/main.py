# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc122/tasks/abc122_d
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
    s = input()
    b, c = [int(char) for char in input().split()]
    n = int(input())
    area = [[int(char) for char in input().split()] for _ in range(n)]


if __name__ == '__main__':
    main()
