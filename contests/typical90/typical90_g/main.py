# -*- coding: utf-8 -*-
from sys import stdin
import bisect
import copy
'''
https://atcoder.jp/contests/typical90/tasks/typical90_g
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
INF = 2 ** 60
n = int(stdin.readline().rstrip())
a = [int(char) for char in stdin.readline().rstrip().split()]
a = sorted(a)
q = int(stdin.readline().rstrip())
for _ in range(q):
    b = int(stdin.readline().rstrip())
    idx = bisect.bisect_left(a, b)
    # print(idx, b, bb)
    res = INF
    if idx < n:
        res = min(res, abs(b - a[idx]))
    if idx > 0:
        res = min(res, abs(b - a[idx-1]))

    print(res)
