# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc267/tasks/abc267_b
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
    s = [int(c) for c in list(input())]
    # print(s[0])
    columns = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
    if s[0] == 1:
        print('No')
        return
    num_pin = []
    num_full = []
    for i in range(len(columns)):
        c = columns[i]
        num = len(c)
        for n in c:
            if s[n] == 0:
                num -= 1
        num_pin.append(num)
        if num == 0:
            num_full.append(i)
    # print(num_pin, num_full)
    # for n in num_full:
    #     if n > 0 and n < len(columns)-1 and num_pin[n-1] > 0 and num_pin[n+1] > 0:
    #         print("Yes")
    #         return
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
