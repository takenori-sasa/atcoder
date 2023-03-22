# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
import sys
from bisect import bisect_left, bisect_right
import math
import copy
from itertools import permutations, combinations
INF = float('inf')
MOD = 10**9+7
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n, k = list(map(int, input().split()))
    a = {i: int(x)for i, x in enumerate(input().split())}
    highest = {0: 0}
    high = a[0]
    for i in range(1, n):
        if a[highest[i-1]] <= a[i]:
            highest[i] = i
            # high = a[i]
        else:
            highest[i] = highest[i-1]
    # print(highest)
    ans = INF
    # print(list(a.values()))

    for i in range(pow(2, n)):
        seen = set()
        for j in range(n):
            if i >> j & 1:
                seen.add(j)
        if len(seen) < k:
            continue
        # print(len(seen), seen)
        b = copy.deepcopy(a)
        bighest = copy.deepcopy(highest)
        cost = 0
        for j in range(n):
            if i >> j & 1:
                if j == bighest[j]:
                    continue
                cost += b[bighest[j]]+1-b[j]
                b[j] = b[bighest[j]]+1
                # bighest[j] = j
                for k in range(1, n):
                    if b[bighest[k-1]] <= b[k]:
                        bighest[k] = k
                        # high = a[i]
                    else:
                        bighest[k] = bighest[k-1]
        ans = min(ans, cost)
        # print(seen, list(b.values()))
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
