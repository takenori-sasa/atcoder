# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc268/tasks/abc268_d
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations, product
INF = float('inf')
MOD = 10**9+7
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n, m = list(map(int, input().split()))
    s = []
    for _ in range(n):
        s.append(input())
    t = set()
    for _ in range(m):
        t.add(input())
    # print(t)
    for perm in permfull(s):
        l_perm = max(len(''.join(list(perm))), 0)
        unders = []
        l_u = 16-l_perm
        l_u -= len(perm)
        l_u += 1
        for i in range(1, l_u+1):
            unders.append('_'*i)
        # print(l_u)
        for bar in product(unders, repeat=len(perm)-1):
            print(perm, bar)
            x = ''
            for i in range(len(bar)):
                x += perm[i]
                x += bar[i]
            x += perm[-1]
            # print(x)
            if len(x) < 3 or len(x) > 16:
                continue
            if x not in t:
                print(x)
                return
    print(-1)

    # if len(perm) == 1:
    #     x = perm[0]


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
