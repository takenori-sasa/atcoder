# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc291/tasks/abc291_d
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 10**9+7
MOD = 998244353
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ab = list(map(int, input().split()))
        a.append((ab[0]))
        b.append((ab[1]))
    an = [0]*n
    bn = [0]*n
    an[0] = 1
    bn[0] = 1
    prea = a[0]
    preb = b[0]
    for i in range(1, n):
        if prea != a[i]:
            an[i] += an[i-1]
        if prea != b[i]:
            bn[i] += an[i-1]
        if preb != b[i]:
            bn[i] += bn[i-1]
        if preb != a[i]:
            an[i] += bn[i-1]
        an[i] %= MOD
        bn[i] %= MOD
        prea = a[i]
        preb = b[i]
    abn = an[-1]+bn[-1]
    abn %= MOD
    print(abn)


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


def elevangle(x, y):
    return math.degrees(math.atan2(y, x))


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
