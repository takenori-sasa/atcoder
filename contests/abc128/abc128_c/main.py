# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc128/tasks/abc128_c
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
    n, m = [int(_x) for _x in input().split()]
    d = []
    for i in range(m):
        s = [int(_x) for _x in input().split()]
        s = set(s[1:])
        d.append(s)
    p = [int(_x) for _x in input().split()]
    cnt = 0
    for i in range(pow(2, n)):
        all_on = True
        bright = bin(i)[2:]
        bright = '0'*(n-len(bright))+bright
        # print(bright)
        for j in range(m):  # 電球
            is_bright = True
            n_on = 0
            for k in range(n):
                if bright[k] == '1' and k+1 in d[j]:
                    n_on += 1
            if n_on % 2 != p[j]:
                is_bright = False
            if not is_bright:
                all_on = False
        if all_on:
            cnt += 1
    print(cnt)


'''
    a = {i+1: int(_x) for i, _x in enumerate(input().split())}
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    trans=map(list, zip(*data))
'''


def primes(limit: int, minLimit: int = None):  # エラトステネスのふるい 篩 素数判定
    if minLimit and (minLimit < 0 or minLimit > limit):
        raise ValueError("incorrect minLimit")
    isPrime = [True] * max(limit + 1, 2)
    isPrime[0] = False
    isPrime[1] = False
    for p in range(2, limit + 1):
        if not isPrime[p]:
            continue
        for i in range(p * p, limit + 1, p):
            isPrime[i] = False
    if minLimit:
        return [i for i, x in enumerate(isPrime[minLimit:], start=minLimit) if x]
    else:
        return [i for i, x in enumerate(isPrime) if x]


def bifull(__bilist__):
    _num_ = len(__bilist__)
    _ret_ = []
    for k in range(_num_+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(set(comb))
    return _ret_


def elevangle(x, y):
    return math.degrees(math.atan2(y, x))


def accm(li):  # 累積 るいせき
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

# def main():
#     n, m = [int(char) for char in input().split()]
#     lump = []
#     for _ in range(m):
#         s = [int(char)-1 for char in input().split()]
#         lump.append(set(s[1:]))
#     p = [int(char) for char in input().split()]
#     # print(*lump, sep="\n")
#     cnt = 0
#     for i in range(n+1):
#         for comb in combinations(range(n), i):
#             # print('start', comb)
#             is_on = True
#             for j in range(m):
#                 num_on = 0
#                 for lu in lump[j]:
#                     if lu in comb:
#                         num_on += 1
#                 if num_on % 2 != p[j]:
#                     is_on = False
#             if is_on:
#                 # print('cnt', comb)
#                 cnt += 1
#
#     print(cnt)
#
#
# if __name__ == '__main__':
#     main()
