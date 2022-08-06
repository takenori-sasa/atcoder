# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc263/tasks/abc263_d
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

    n, l, r = [int(char) for char in input().split()]
    a = [int(char) for char in input().split()]
    sum_a = sum(a)
    accl = [l-a[0]]
    accr = [r-a[-1]]
    for i in range(1, n):
        accl.append(accl[-1]+l-a[i])
    for i in range(2, n+1):
        accr.append(accr[-1]+r-a[-i])
    min_l = [0]
    min_acc = accl[0]
    for i in range(1, n):
        if accl[i] < min_acc:
            min_acc = accl[i]
            min_l.append(i)
        else:
            min_l.append(min_l[-1])
    min_r = [0]
    min_acc = accr[0]
    for i in range(1, n):
        if accr[i] < min_acc:
            min_acc = accr[i]
            min_r.append(i)
        else:
            min_r.append(min_r[-1])
    min_r = [n-1-m for m in min_r]
    # min_r.reverse()
    print(accl, accr)
    print(min_l, min_r)

    # if min_l >= 0 and min_r >= 0:
    #     print(sum_a)
    # elif min_l >= 0:
    #     min_idx = min([i for i, v in enumerate(accr) if v == min(accr)])+1
    #     print(sum_a-r*(n-min_idx))
    # elif min_r >= 0:
    #     min_idx = max([i for i, v in enumerate(accl) if v == min(accl)])+1
    #     print(sum_a-r*(min_idx))
    # elif l < r:
    #     xx = [i for i, v in enumerate(accl) if v == min(accl)]
    #
    #     for x in range(xx):
    #         pass
    #     y = max([i for i, v in enumerate(accl) if v == min(accl) and])+1


if __name__ == '__main__':
    main()
