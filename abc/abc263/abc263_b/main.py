# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc263/tasks/abc263_b
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
    n = int(input().rstrip())
    p = [int(char)-1 for char in input().split()]
    me = p[-1]
    ans = 1
    while me != 0:
        me = p[me-1]
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
