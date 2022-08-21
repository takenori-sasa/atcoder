# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc265/tasks/abc265_c
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
    pass
    h, w = [int(char) for char in input().split()]
    area = [input() for _ in range(h)]
    visited = [[-1]*w for _ in range(h)]
    x, y = 0, 0
    # visited[0][0] = 0
    while True:
        # print(x, y)
        if visited[x][y] == 0:
            print(-1)
            return
        visited[x][y] = 0
        if area[x][y] == 'U' and x != 0:
            x, y = x-1, y
        elif area[x][y] == 'D' and x != h-1:
            x, y = x+1, y
        elif area[x][y] == 'R' and y != w-1:
            x, y = x, y+1
        elif area[x][y] == 'L' and y != 0:
            x, y = x, y-1
        else:
            print(x+1, y+1)
            return


if __name__ == '__main__':
    main()
