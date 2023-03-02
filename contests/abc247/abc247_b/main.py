# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc247/tasks/abc247_b
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 998244353
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n = int(input())
    s = []
    t = []
    n_t = {}
    for i in range(n):
        a, b = list(map(str, input().split()))
        s.append(a)
        t.append(b)
    # set_s = set(s)
    # set_t = set(t)
    # print(s, t)
    ans = 'Yes'
    for i in range(n):
        a = s[i]
        b = t[i]
        flag_s = False
        flag_t = False
        for j in range(n):
            if i == j:
                continue
            # print(a, s[j], a == s[j], b, t[j], b == t[j])
            if a == s[j] or a == t[j]:
                flag_s = True
            if b == s[j] or b == t[j]:
                flag_t = True
        # print(a, flag_s, b, flag_t)
        if flag_s and flag_t:
            # print(a,  b)
            ans = 'No'
            break
    print(ans)


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
