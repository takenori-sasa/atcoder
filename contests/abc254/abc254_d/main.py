# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc254/tasks/abc254_d
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
from heapq import heappush, heappop
from collections import deque
INF = float('inf')
MOD = 998244353
'''
    s = input()
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
    grid = [[int(_x) for _x in input().split()] for _ in range(n)]
'''


def main():
    n = int(input())
    # n = 4
    squares = set()
    # square_dict = {}
    ans = 0
    rest = {}
    divisors = {}
    for i in range(1, n+1):
        if i*i > n:
            break
        # square_dict[i] = pow(i, 2)
        squares.add(pow(i, 2))
    for i in range(1, n+1):
        divisors[i] = make_divisors(i)
    # for i in range(1, n+1):
    #     k = i//max_square_divisior(i, squares)
    #     if k not in rest:
    #         rest[k] = 0
    #     rest[k] += 1
    # for k in rest:
    #     ans += pow(rest[k], 2)
    # for i in range(1, n+1):
    #     for d in reversed(divisors[i]):
    #         if d in squares:
    #             if i//d not in rest:
    #                 rest[i//d] = 0
    #             rest[i//d] += 1
    #             break
    # for v in rest.values():
    #     ans += pow(v, 2)

    print(ans)


'''
    a = {i+1: int(_x) for i, _x in enumerate(input().split())}
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    tenchi = list(zip(*matrix))
'''


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


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
