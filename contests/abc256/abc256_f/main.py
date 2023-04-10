# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc256/tasks/abc256_f
from itertools import permutations, combinations, accumulate, groupby
import sys
import os
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


def lcm(x: int, y: int) -> int:
    '''
    lcm
    '''
    return (x * y) // math.gcd(x, y)


def debugger(*args, end="\n"):
    if os.environ.get('DLOCAL') == '1':
        print(*args, end=end)


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


class ModEnum():
    # modつき数え上げ
    # 順列perm
    # 組み合わせcomb
    # 重複組合せcomb_with
    # 階乗fact
    def __init__(self, mod=10**9 + 7):
        self.mod = mod
        self._factorial = [1]
        self._size = 1
        self._factorial_inv = [1]
        self._size_inv = 1

    def __call__(self, n):
        '''n! % mod '''
        return self.fact(n)

    def fact(self, n: int) -> int:
        '''n! % mod '''
        if n >= self.mod:
            return 0
        self.__make__(n)
        return self._factorial[n]

    def __fact_inv__(self, n):
        '''n!^-1 % mod '''
        if n >= self.mod:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        self.__make_inv__(n)
        return self._factorial_inv[n]

    def pow(self, base: int, exponent: int) -> int:
        return pow(base, exponent, self.mod)

    def comb(self, n: int, r: int) -> int:
        ''' nCr % mod '''
        if r > n:
            return 0
        t = self.__fact_inv__(n-r)*self.__fact_inv__(r) % self.mod
        return self(n)*t % self.mod

    def comb_with_repetition(self, n: int, r: int) -> int:
        ''' nHr % mod '''
        t = self.__fact_inv__(n-1)*self.__fact_inv__(r) % self.mod
        return self(n+r-1)*t % self.mod

    def perm(self, n: int, r: int) -> int:
        ''' nPr % mod '''
        if r > n:
            return 0
        return self(n)*self.__fact_inv__(n-r) % self.mod

    @staticmethod
    def __xgcd__(a, b):
        ''' return (g, x, y) such that a*x + b*y = g = gcd(a, b) '''
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def __modinv__(self, n: int) -> int:
        g, x, _ = self.__xgcd__(n, self.mod)
        if g != 1:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        return x % self.mod

    def __make__(self, n):
        if n >= self.mod:
            n = self.mod
        if self._size < n+1:
            for i in range(self._size, n+1):
                self._factorial.append(self._factorial[i-1]*i % self.mod)
            self._size = n+1

    def __make_inv__(self, n):
        if n >= self.mod:
            n = self.mod
        self.__make__(n)
        if self._size_inv < n+1:
            for i in range(self._size_inv, n+1):
                self._factorial_inv.append(self.__modinv__(self._factorial[i]))
            self._size_inv = n+1


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    main()
