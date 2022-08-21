# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/arc096/tasks/arc096_a
    for _ in range(n):
        a = [int(char) for char in input().split()]
    data = [input().split() for _ in range(n)]
    print(*ans, sep="\n")
転置
    trans=map(list, zip(*data))
'''
INF = float('inf')
# MOD = 10**9+7


def main():
    a, b, c, x, y = [int(char) for char in input().split()]
    price = INF
    for i in range(max(x, y)+1):
        price = min(price, max(0, a*(x-i))+max(0, b*(y-i))+c*2*i)
    print(price)


if __name__ == '__main__':
    main()
