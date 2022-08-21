# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc264/tasks/abc264_b
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
    r, c = [int(char) for char in input().split()]
    if min(r, 15-r+1) <= c and max(15-r+1, r) >= c:
        if r % 2 == 0:
            print('white')
        else:
            print('black')
    else:
        if c % 2 == 0:
            print('white')
        else:
            print('black')


if __name__ == '__main__':
    main()
