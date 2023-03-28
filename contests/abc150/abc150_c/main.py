# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
import itertools
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc150/tasks/abc150_c
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
INF = float('inf')
# MOD = 10**9+7


def main():
    n = int(input().rstrip())
    r = [int(char)-1 for char in input().split()]
    q = [int(char)-1 for char in input().split()]
    a = INF
    b = INF
    for i, perm in enumerate(itertools.permutations(range(n))):
        # print(list(perm))
        if r == list(perm):
            a = i
        if q == list(perm):
            b = i
    print(abs(a-b))


if __name__ == '__main__':
    main()
