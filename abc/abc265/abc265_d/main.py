# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc265/tasks/abc265_d
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
    n, p, q, r = [int(char) for char in input().split()]
    a = [int(char) for char in input().split()]
    acc = [0]
    for i in range(n):
        acc.append(a[i]+acc[-1])
    n_acc = len(acc)
    # print(sum(a), acc)
    ans = 'No'
    for x in range(n):
        y = bisect_left(acc, acc[x]+p)
        z = bisect_left(acc, acc[x]+p+q)
        w = bisect_left(acc, acc[x]+p+q+r)
        if w >= n_acc or z >= n_acc or y >= n_acc:
            # print(x, 'out')
            continue
        # print(x, y, z, w)
        # print(acc[y]-acc[x], acc[z]-acc[y], acc[w]-acc[z])
        if acc[x]+p == acc[y] and acc[x]+p+q == acc[z] and acc[x]+p+q+r == acc[w]:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
