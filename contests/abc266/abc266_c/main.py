# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc266/tasks/abc266_c
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
    x = []
    y = []
    for _ in range(4):
        xy = [int(char) for char in input().split()]
        x.append(xy[0])
        y.append(xy[1])
    x += x
    y += y
    # print(x)
    # print(y)
    for i in range(1, len(y)-1):
        vec1 = [x[i-1]-x[i], y[i-1]-y[i]]
        vec2 = [x[i+1]-x[i], y[i+1]-y[i]]
        deg1 = math.degrees(math.atan2(vec1[1], vec1[0]))
        deg2 = math.degrees(math.atan2(vec2[1], vec2[0]))
        deg = deg2-deg1
        # print(i, deg)
        if deg < 0:
            deg += 360
        # print(i, deg)
        if deg < 180:
            print('No')
            return

    print('Yes')


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
