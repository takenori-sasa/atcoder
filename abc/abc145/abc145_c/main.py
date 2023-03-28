# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 10**9+7
'''
https://atcoder.jp/contests/abc145/tasks/abc145_c
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    sum_dist = 0
    cnt = 0
    for perm in permutations(range(n)):
        # print(perm)
        dist = 0
        x, y = xy[perm[0]][0], xy[perm[0]][1]
        for i in perm:
            xx, yy = xy[i][0], xy[i][1]
            # print(xx, yy, x, y)
            dist += math.sqrt((xx-x)**2+(yy-y)**2)
            x, y = xx, yy
            # print(dist)
        sum_dist += dist
        cnt += 1
    print(sum_dist/cnt)


'''
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    trans=map(list, zip(*data))
'''


def bifull(__bilist__):
    _num_ = len(__bilist__)
    _ret_ = []
    for k in range(_num_+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(set(comb))
    return _ret_


def accm(li):
    _ret_ = [0]
    _num_ = len(li)
    for i in range(_num_):
        _ret_.append(_ret_[-1]+li[i])
    return _ret_


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    main()
