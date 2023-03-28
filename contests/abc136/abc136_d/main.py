# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc136/tasks/abc136_d
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
    l = [0]
    for c in s:
        if c == 'R':
            if l[-1] > 0:
                l[-1] += 1
            else:
                l.append(1)
        else:
            if l[-1] < 0:
                l[-1] -= 1
            else:
                l.append(-1)
    l = l[1:]
    l = l[::-1]
    ans = []
    while len(l) > 0:
        r = l.pop()
        h = -l.pop()
        ans += ['0']*(r-1)
        pr = (r+1)//2+h//2
        pl = r//2+(h+1)//2
        ans += [str(pr), str(pl)]
        ans += ['0']*(h-1)
    print(' '.join(ans))


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
