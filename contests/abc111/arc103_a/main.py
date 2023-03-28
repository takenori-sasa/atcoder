# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc111/tasks/arc103_a
from itertools import permutations, combinations, accumulate, groupby
import sys
from bisect import bisect_left, bisect_right
import math
from heapq import heappush, heappop
from collections import deque
INF = float('inf')
MOD = 998244353
# MOD = pow(10, 9)+7
DXY4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
DXY8 = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

'''
    s = input().rstrip()
    s,t = [c for c in input().rstrip().split()]
    field = [''.join(input().rstrip().split()) for _ in range(n)]
    grid = [[int(_x) for _x in input().rstrip().split()] for _ in range(n)]
'''


def main():
    n = int(input().rstrip())
    v = [int(_x) for _x in input().rstrip().split()]
    cnt = {}
    even = {}
    odd = {}
    for i in range(n):
        if i % 2 != 0:
            if v[i] not in even:
                even[v[i]] = 0
            even[v[i]] += 1
        else:
            if v[i] not in odd:
                odd[v[i]] = 0
            odd[v[i]] += 1
    # print(odd, even)
    odd = sorted(odd.items(), key=lambda x: x[1])
    even = sorted(even.items(), key=lambda x: x[1])
    ok, ov = odd.pop()
    ek, ev = even.pop()
    if ok != ek:
        print(n-ov-ev)
        return
    if len(odd) == 0 and len(even) == 0:
        print(abs(ov))
    elif len(odd) == 0:
        ek, ev = even.pop()
        print(n-ov-ev)
    elif len(even) == 0:
        ok, ov = odd.pop()
        print(n-ov-ev)
    else:
        okk, ovv = odd.pop()
        ekv, evv = even.pop()
        print(min(n-ov-evv, n-ev-ovv))
    # print(cnt)
    # if len(cnt) == 1:
    #     print(n//2)
    #     return
    # v = list(cnt.values())
    # v.sort()
    # first = v.pop()
    # second = v.pop()
    # if len(v) == 0:
    #     print(abs(n//2-first))
    #     return
    # print(n-first-second)


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


def permfull(arr, num: int = -1):  # 順列全探索
    _num_ = len(arr)
    _ret_ = []
    if num == -1:
        num = _num_
    for perm in permutations(arr, num):
        _ret_.append(list(perm))
    return _ret_


def lcm_calc(x, y):
    return (x * y) // math.gcd(x, y)


def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    # RUN LENGTH ENCODING str -> list(tuple()) ランレングス ランレンクス
    # example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def runLengthDecode(L: "list[tuple]") -> str:
    # RUN LENGTH DECODING list(tuple()) -> str  ランレングス ランレンクス
    # example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
    res = ""
    for c, n in L:
        res += c * int(n)
    return res


def runLengthEncodeToString(S: str) -> str:
    # RUN LENGTH ENCODING str -> str ランレングス ランレンクス
    # example) "aabbbbaaca" -> "a2b4a2c1a1"
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    main()
