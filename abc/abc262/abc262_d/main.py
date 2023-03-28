# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc262/tasks/abc262_d
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b, c = [int(char) for char in stdin.readline().rstrip().split()]
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip()] for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(n)]
print(*ans, sep="\n")
'''
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


n = int(stdin.readline().rstrip())
num = {i: 0 for i in range(1, n+1)}
a = [int(char) for char in stdin.readline().rstrip().split()]
app = {}
MOD = 998244353
ans = 0
# print(num)
for i in range(n):
    app[i+1] = {}
    ap = app[i+1]
    for j in range(n):
        if (a[j] % (i+1)) not in ap:
            ap[a[j] % (i+1)] = 0
        ap[a[j] % (i+1)] += 1
for k, v in app.items():
