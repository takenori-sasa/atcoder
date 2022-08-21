# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc263/tasks/abc263_c
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


def dfs(n, ans, rest):
    if len(ans) == n:
        print(' '.join([str(c) for c in ans])+' ')
        return
    else:
        for i in range(len(rest)):
            dfs(n, ans+[rest[i]], rest[i+1:])


def main():

    n, m = [int(char) for char in input().split()]
    seq = [i+1 for i in range(m)]
    for i in range(m-n+1):
        # print([seq[i]], seq[i+1:])
        dfs(n, [seq[i]], seq[i+1:])


if __name__ == '__main__':
    main()
