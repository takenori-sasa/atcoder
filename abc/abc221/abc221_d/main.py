# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc221/tasks/abc221_d
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
    a = [int(_x) for _x in input().rstrip().split()]


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


class HeapDict:
    # cf.https://tsubo.hatenablog.jp/entry/2020/06/15/124657
    # O(logN)で挿入削除,O(1)でmin,exist?
    # 二分探索ムリ
    # multisetの代わり
    def __init__(self):
        self.h = []
        self.d = dict()

    def insert(self, x):
        heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def remove(self, x):
        if x not in self.d or self.d[x] == 0:
            print(x, "is not in HeapDict")
            exit()
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

    def min(self):
        return self.get_min()


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    main()
