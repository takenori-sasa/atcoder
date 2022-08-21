# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc263/tasks/abc263_a
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
    a = [int(char) for char in input().split()]
    trump = [0]*13
    for num in a:
        trump[num-1] += 1
    pool = set(trump)
    if pool == set([0, 2, 3]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()