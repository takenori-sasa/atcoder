# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc202/tasks/abc202_b
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
    s = input()
    s = s[::-1]
    t = ''
    # 0 を 0 に、1 を 1 に、6 を 9 に、8 を 8 に、9 を 6 に変換する。
    for c in s:
        if c == '6':
            t += '9'
        elif c == '9':
            t += '6'
        else:
            t += c
    print(t)


'''
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    trans=map(list, zip(*data))
'''


def prime(N):  # エラトステネスのふるい 篩 素数判定
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes


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
