# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc265/tasks/abc265_e
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
MAX = 10**9


def main():
    pass
    n, m = [int(char) for char in input().split()]
    a, b, c, d, e, f = [int(char) for char in input().split()]
    obstacle = set()
    cords = []
    for _ in range(m):
        x, y = [int(char) for char in input().split()]
        obstacle.add((x, y))
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i+j+k == n:
                    cords.append((a*i+c*j+e*k, b*i+d*j+f*k))
    dp = [[list(range(-MAX, MAX+1)) for _ in range(-MAX, MAX+1)]
          for __ in range(n)]
    # for _ in range()
    # print(list(range(-5, 5)))


if __name__ == '__main__':
    main()
