# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc201/tasks/abc201_c
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
from heapq import heappush, heappop
from collections import deque
INF = float('inf')
MOD = 998244353
# MOD = pow(10, 9)+7
DXY4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
DXY8 = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

'''
    s,t = [c for c in input().rstrip().split()]
    field = [''.join(input().rstrip().split()) for _ in range(n)]
    grid = [[int(_x) for _x in input().rstrip().split()] for _ in range(n)]
'''


def main():
    s = input().rstrip()
    use = set()
    not_use = set()
    vague = set()
    for i in range(len(s)):
        if s[i] == 'o':
            use.add(str(i))
        elif s[i] == 'x':
            not_use.add(str(i))
        if s[i] == '?':
            vague.add(str(i))
    cnt = 0
    # print(use, not_use, vague)
    for i in range(10000):
        t = '0'*(4-len(str(i)))+str(i)
        t = set(list(t))

        # if t >= use:

        # print(t, t >= use)
        if t.issuperset(use) and t.isdisjoint(not_use):
            cnt += 1
    print(cnt)


'''
    a = {i+1: int(_x) for i, _x in enumerate(input().split())}
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    tenchi = list(zip(*matrix))
'''


# エラトステネスのふるい 篩 素数判定
def primes(limit: int, minLimit: int = None):
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


def bitfull(__bilist__):  # bit全探索 組み合わせ全探索
    _num_ = len(__bilist__)
    _ret_ = []
    for k in range(_num_+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(list(comb))
    return _ret_


def elevangle(x, y):  # 仰角 俯角 ぎょうかく ふかく
    return math.degrees(math.atan2(y, x))


def accm(li):  # 累積和 るいせき
    _ret_ = [0]
    _num_ = len(li)
    for i in range(_num_):
        _ret_.append(_ret_[-1]+li[i])
    return _ret_


def permfull(arr, num: int = -1):  # 順列全探索
    _num_ = len(arr)
    _ret_ = []
    if num == -1:
        num = _num_
    for perm in permutations(arr, num):
        _ret_.append(list(perm))
    return _ret_


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    main()
