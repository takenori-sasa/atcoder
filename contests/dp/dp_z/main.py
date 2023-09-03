# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/dp/tasks/dp_z
from itertools import permutations, combinations, groupby, product
import sys
import os
from bisect import bisect_left, bisect_right
import math
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict as ddict, Counter
import pprint
from typing import ItemsView


def main():
    a = [int(_x) for _x in input().rstrip().split()]


'''
    s = input().rstrip()
    n = int(input().rstrip())
    field = [list(''.join(input().rstrip().split())) for _ in range(h)]
    grid = [[int(_x) for _x in input().rstrip().split()] for _ in range(h)]
    tenchi = list(zip(*matrix))
    print(''.join(map(str, list(L))))
    li = sorted(li, reverse=True, key=lambda x: x[1])
    a = {i+1: int(_x) for i, _x in enumerate(input().split())}
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
'''

dict = ddict
INF = float('inf')
MOD = 998244353
MOD10 = 1000000007
MOD99 = 998244353
# MOD = MOD99
YES = 'Yes'
NO = 'No'
DXY4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
DXY8 = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
alphabet = 'abcdefghijklmnopqrstuvwxyz'.lower()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.upper()


def primes(n: int, psieve=None):
    '''素因数列挙'''
    if psieve is None:
        psieve = sieve(n)
    cnt = Counter()
    while n >= 2:
        cnt[psieve[n]] += 1
        n //= psieve[n]
    return list(cnt.keys())


def factorize(n: int, psieve=None):
    '''素因数分解'''
    if psieve is None:
        psieve = sieve(n)
    cnt = Counter()
    while n >= 2:
        cnt[psieve[n]] += 1
        n //= psieve[n]
    return list(cnt.items())


def sieve(n: int):
    '''エラトステネスのふるい'''
    # TODO 区間ふるい
    maxAS = n
    eratree = [0] * (maxAS + 10)
    for p in range(2, maxAS + 1):
        if eratree[p]:
            continue
        # p is prime
        eratree[p] = p
        x = p * p
        while x <= maxAS:
            if not eratree[x]:
                eratree[x] = p
            x += p
    return eratree


def divisors(n):
    '''約数リスト'''
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def bitfull(__bilist__):
    '''bit全探索'''
    num = len(__bilist__)
    _ret_ = []
    for k in range(num+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(list(comb))
    return _ret_


def elevangle(x, y):
    '''仰角 俯角 ぎょうかく ふかく'''
    return math.degrees(math.atan2(y, x))


def permfull(arr, num: int = -1):
    '''順列全探索'''
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


def flushprint(*args, end="\n"):
    print(*args, end=end, flush=True)


def runLengthEncode(S: str):
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
        self.d = ddict()

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


def Tenthbase_to_NthBase(num: int, base: int):
    '''10進数からn進数'''
    X_dumy = num
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % base)+out
        X_dumy = X_dumy//base
    return out


def NthBase_to_TenthBase(num: str, base: int):
    '''n進数→10進数'''
    out: int = 0
    for i in range(1, len(str(num))+1):
        out += int(num[-i])*(base**(i-1))
    return out


class ModMath():
    '''modつき数え上げ'''
    # 順列perm
    # 組み合わせcomb
    # 重複組合せcomb_with
    # 階乗fact

    def __init__(self, mod=MOD):
        self.mod = mod
        self._factorial = [1]
        self._size = 1
        self._factorial_inv = [1]
        self._size_inv = 1

    def __call__(self, n):
        '''n! % mod '''
        return self.fact(n)

    def fact(self, n):
        '''n! % mod '''
        if n >= self.mod:
            return 0
        self._make(n)
        return self._factorial[n]

    def fact_inv(self, n):
        '''n!^ -1 % mod '''
        if n >= self.mod:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        self._make_inv(n)
        return self._factorial_inv[n]

    def comb(self, n, r):
        ''' nCr % mod '''
        if r > n:
            return 0
        t = self.fact_inv(n-r)*self.fact_inv(r) % self.mod
        return self(n)*t % self.mod

    def comb_with_repetition(self, n, r):
        ''' nHr % mod '''
        t = self.fact_inv(n-1)*self.fact_inv(r) % self.mod
        return self(n+r-1)*t % self.mod

    def perm(self, n, r):
        ''' nPr % mod '''
        if r > n:
            return 0
        return self(n)*self.fact_inv(n-r) % self.mod

    @staticmethod
    def xgcd(a, b):
        ''' return (g, x, y) such that a*x + b*y = g = gcd(a, b) '''
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def modinv(self, n):
        g, x, _ = self.xgcd(n, self.mod)
        if g != 1:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        return x % self.mod

    def _make(self, n):
        if n >= self.mod:
            n = self.mod
        if self._size < n+1:
            for i in range(self._size, n+1):
                self._factorial.append(self._factorial[i-1]*i % self.mod)
            self._size = n+1

    def _make_inv(self, n):
        if n >= self.mod:
            n = self.mod
        self._make(n)
        if self._size_inv < n+1:
            for i in range(self._size_inv, n+1):
                self._factorial_inv.append(self.modinv(self._factorial[i]))
            self._size_inv = n+1


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        return self.find(x)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = ddict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


class Graph():
    def __init__(self, n: int, direct=False):
        self.size = n
        self.is_directed = direct
        self.adjlist = [[] for _ in range(self.size)]
        self.edge = []

    def graph(self):
        return self.adjlist

    def connect(self, start: int, goal: int, weight: int = 1):
        self.adjlist[start-1].append((goal-1, weight))
        if not self.is_directed:
            self.adjlist[goal-1].append((start-1, weight))
        self.edge.append([weight, (start-1, goal-1)])

    def create_adjmatrix(self):
        self.adjmatrix = [[INF]*self.size for _ in range(self.size)]
        # テーブルを初期化: 同じ頂点は重み0 かつ　隣接グラフG[From][To]=weight　を入力
        for frm in range(self.size):
            self.adjmatrix[frm][frm] = 0  # 初期化1 同じ頂点は重み0
            for to, weight in self.adjlist[frm]:
                self.adjmatrix[frm][to] = weight

    def kruskal(self, mininum: bool = True):
        '''クラスカル法 最小全域木 O(ElogV)'''
        graph = self.graph
        size = len(graph.size)
        edges = graph.edge
        edges.sort(reverse=not mininum)  # 重みが小さい順に辺をソートする
        ans: int = 0  # 最小全域木の重み
        uf = UnionFind(size)  # UnionFindを初期化. 初期は全頂点が異なるグループ
        for w, (From, To) in edges:

            # 同じグループ(木)に属する場合、その辺は無視する
            if uf.same(From, To):
                continue
            # 異なるグループの場合、その辺を採用し、頂点From, Toを同じグループにする
            else:
                ans += w
                uf.unite(From, To)
        return ans


def dijkstra(start: int, goal: int, graph: Graph):
    '''ダイスクトラ O(ElogV)'''
    def trace(s, t, ancestors):
        route = [t]
        c = t
        while True:
            a = ancestors[c]
            assert a is not None, 'Failed to trace'
            route.append(a)
            if a == s:
                break
            c = ancestors[c]
        route.reverse()
        return route
    # graph = graph.adjlist
    heap = [(*l, start) for l in graph.adjlist[start]]
    heapify(heap)
    visited = set()
    ancestors = [None] * len(graph.adjlist)
    while heap:
        node, cost, ancestor = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        ancestors[node] = ancestor
        if node == goal:
            return cost, trace(start, goal, ancestors)
        for cost2, node2 in graph.adjlist[node]:
            if node2 not in visited:
                heappush(heap, (node2, cost + cost2, node))
    return INF, None


def Warshall_Floid(G: Graph):
    '''ワーシャルフロイド O(E ^ 3)'''
    G.create_adjmatrix()
    dist = G.adjmatrix
    num_nodes = len(G.adjlist)  # 頂点数

    # フロイドワーシャル法のコア部分
    for k in range(num_nodes):
        for From in range(num_nodes):
            for To in range(num_nodes):
                if dist[From][k] + dist[k][To] < dist[From][To]:
                    dist[From][To] = dist[From][k] + dist[k][To]

    # 負閉路の検出 dist[i][i]<0となる頂点iがあれば負閉路が存在
    NEGATIVE_CYCLE = False
    for i in range(num_nodes):
        if dist[i][i] < 0:
            NEGATIVE_CYCLE = True
            break

    return dist, NEGATIVE_CYCLE


class WeightedUnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


class CompressedMultiSet:
    # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
    # multi: マルチセットか通常のOrderedSetか
    # まずクエリ先読みして必要な座標洗い出してinitせよ
    def __init__(self, n=0, *, compress=[], multi=True):
        self.multi = multi
        self.inv_compress = sorted(set(compress)) if len(
            compress) > 0 else [i for i in range(n)]
        self.compress = {k: v for v, k in enumerate(self.inv_compress)}
        self.counter_all = 0
        self.counter = [0] * len(self.inv_compress)
        self.bit = BIT(len(self.inv_compress))

    def add(self, x, n=1):     # O(log n)
        if not self.multi and n != 1:
            raise KeyError(n)
        x = self.compress[x]
        count = self.counter[x]
        if count == 0 or self.multi:  # multiなら複数カウントできる
            self.bit.add(x + 1, n)
            self.counter_all += n
            self.counter[x] += n

    def remove(self, x, n=1):  # O(log n)
        if not self.multi and n != 1:
            raise KeyError(n)
        x = self.compress[x]
        count = self.bit.get(x + 1)
        if count < n:
            raise KeyError(x)
        self.bit.add(x + 1, -n)
        self.counter_all -= n
        self.counter[x] -= n

    def __repr__(self):
        return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'

    def __len__(self):         # oprator len: O(1)
        return self.counter_all

    def count(self, x):        # O(1)
        return self.counter[self.compress[x]] if x in self.compress else 0

    def __getitem__(self, i):  # operator []: O(log n)
        if i < 0:
            i += len(self)
        x = self.bit.lower_bound(i + 1)
        if x > self.bit.n:
            raise IndexError('list index out of range')
        return self.inv_compress[x - 1]

    def __contains__(self, x):  # operator in: O(1)
        return self.count(x) > 0

    def bisect_left(self, x):  # O(log n)
        return self.bit.sum(bisect_left(self.inv_compress, x))

    def bisect_right(self, x):  # O(log n)
        return self.bit.sum(bisect_right(self.inv_compress, x))


class BIT:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n:
                a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:                    # nは大きさ
            self.d = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f'[{l}, {r}]:{self.d[r]}')
            res.append(' '.join(res2))
            p >>= 1
        res.append(
            f'{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}')
        return '\n'.join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d[p] += x
            p += p & -p

    def get(self, p, default=None):     # O(log(n))
        assert p > 0
        return self.sum(p) - self.sum(p - 1) if 1 <= p <= self.n or default is None else default

    def sum(self, p):     # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d[p]
            p -= p & -p
        return res

    def lower_bound(self, x):   # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        if x <= 0:
            return 0
        p, r = 0, self.size
        while r > 0:
            if p + r <= self.n and self.d[p + r] < x:
                x -= self.d[p + r]
                p += r
            r >>= 1
        return p + 1


def accumulate(arr):
    '''accumulated list'''
    _ret_ = [0]
    for i in range(len(arr)):
        _ret_.append(_ret_[-1]+arr[i])
    return _ret_


class ModInt:

    def __init__(self, x, mod=MOD):
        self.mod = mod
        self.x = x.x if isinstance(x, ModInt) else x % self.mod

    def set_mod(self, mod):
        self.mod = mod

    def pow(self, exponent):
        return ModInt(pow(self.x, exponent, self.mod))

    def __str__(self): return str(self.x)
    __repr__ = __str__
    def __int__(self): return self.x
    __index__ = __int__

    def __add__(self, other): return ModInt(self.x + ModInt(other).x)
    def __sub__(self, other): return ModInt(self.x - ModInt(other).x)
    def __mul__(self, other): return ModInt(self.x * ModInt(other).x)

    def __pow__(self, other): return ModInt(
        pow(self.x, ModInt(other).x, self.mod))
    def __truediv__(self, other): return ModInt(
        self.x * pow(ModInt(other).x, self.mod - 2, self.mod))

    def __floordiv__(self, other): return ModInt(self.x // ModInt(other).x)
    def __radd__(self, other): return ModInt(other + self.x)
    def __rsub__(self, other): return ModInt(other - self.x)
    def __rpow__(self, other): return ModInt(pow(other, self.x, self.mod))
    def __rmul__(self, other): return ModInt(other * self.x)
    def __rtruediv__(self, other): return ModInt(
        other * pow(self.x, self.mod - 2, self.mod))

    def __rfloordiv__(self, other): return ModInt(other // self.x)

    def __lt__(self, other): return self.x < ModInt(other).x
    def __gt__(self, other): return self.x > ModInt(other).x
    def __le__(self, other): return self.x <= ModInt(other).x
    def __ge__(self, other): return self.x >= ModInt(other).x
    def __eq__(self, other): return self.x == ModInt(other).x
    def __ne__(self, other): return self.x != ModInt(other).x


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    main()
