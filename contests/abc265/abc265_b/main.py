# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc265/tasks/abc265_b
    s = stdin.readline().rstrip()
    b, c = [int(char) for char in input().split()]
    a = [int(char) for char in input().split()]
    n = int(input().rstrip())
    for _ in range(n):
        a = [int(char) for char in input().split()]
    data = [input().split() for _ in range(n)]
    data = [[int(char) for char in input().split()] for _ in range(n)]
    data = [[int(char) for char in input().split()] for _ in range(n)]
    print(*ans, sep="\n")
転置
    trans=map(list, zip(*data))
'''
# INF = float('inf')
# MOD = 10**9+7


def main():
    n, m, t = [int(char) for char in input().split()]
    a = [int(char) for char in input().split()]
    bonus = {}
    for _ in range(m):
        x, y = [int(char) for char in input().split()]
        bonus[x-1] = y
    ans = 'Yes'
    # print(bonus)
    for i in range(n-1):
        if t <= a[i]:
            print('No')
            return
        t -= a[i]
        if i+1 in bonus:
            t += bonus[i+1]
        # print(i, t)
    print('Yes')


if __name__ == '__main__':
    main()
