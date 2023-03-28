# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc147/tasks/abc147_c
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 998244353
'''
    s = input()
    s,t = list(map(str, input().split()))
'''


def main():
    n = int(input())
    honest = []
    liar = []
    for __ in range(n):
        a = int(input())
        h = set()
        l = set()
        for _ in range(a):
            x, y = [int(_x) for _x in input().split()]
            if y == 1:
                h.add(x-1)
            else:
                l.add(x-1)
        honest.append(h)
        liar.append(l)
    # for i in range(n):
    #     print(i, honest[i], liar[i])
    h_max = 0
    for i in range(0, pow(2, n)):
        bi = bin(i)[2:]
        bi = '0'*(n-len(bi))+bi
        all_true = True
        for j in range(len(bi)):
            c_true = True
            if bi[j] == '1':
                for h in honest[j]:
                    if bi[h] == '0':
                        c_true = False
                for l in liar[j]:
                    if bi[l] == '1':
                        c_true = False
            if not c_true:
                all_true = False
        if all_true:
            nh = 0
            for b in bi:
                if b == '1':
                    nh += 1
            h_max = max(h_max, nh)
    print(h_max)


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
