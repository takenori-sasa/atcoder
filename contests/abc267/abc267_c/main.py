# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc267/tasks/abc267_c
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
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    acc = accm(a)
    ex_acc = expect_accm(a)
    # print(acc)
    # print(ex_acc)
    ans = -INF
    for i in range(1, len(acc)-m+1):
        # print(i)
        # if not i+m-1 < len(acc):
        #     continue
        tmp = ex_acc[i+m-1]
        tmp -= ex_acc[i-1]
        # print(i, tmp)
        tmp -= (acc[i+m-1]-acc[i-1])*(i-1)
        # print(i, tmp, acc[i+m-1], acc[i-1])
        ans = max(tmp, ans)
    print(ans)


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


def expect_accm(li):
    _ret_ = [0]
    _num_ = len(li)
    for i in range(_num_):
        _ret_.append(_ret_[-1]+li[i]*(i+1))
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
