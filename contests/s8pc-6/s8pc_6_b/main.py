# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 10**9+7
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    aa = []
    bb = []
    for i in range(n):
        aa.append(ab[i][0])
        bb.append(ab[i][1])
    min_dist = INF
    for s in aa:
        for g in bb:
            dist = 0
            for a, b in ab:
                dist += abs(s-a)+abs(g-b)+abs(a-b)
            min_dist = min(min_dist, dist)
    print(min_dist)


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


def permfull(arr, num=-1):
    _num_ = len(arr)
    _ret_ = []
    if num == -1:
        num = _num_
    for perm in permutations(arr, num):
        _ret_.append(list(perm))
    return _ret_


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    main()
