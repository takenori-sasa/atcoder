# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 998244353
'''
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n, a, b = [int(_x) for _x in input().split()]
    s = input()
    f = a+b
    for i in range(len(s)):
        if s[i] == 'c':
            print('No')
        elif s[i] == 'a':
            if f > 0:
                f -= 1
                print('Yes')
            else:
                print('No')
        else:
            if b > 0 and f > 0:
                b -= 1
                f -= 1
                print('Yes')
            else:
                print('No')


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
