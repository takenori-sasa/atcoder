# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc262/tasks/abc262_e
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
n, m, k = [int(char) for char in stdin.readline().rstrip().split()]
con = {}
for _ in range(m):
    u, v = [int(char) for char in stdin.readline().rstrip().split()]
    if u not in con:
        con[u] = set()
    con[u].add(v)
    if v not in con:
        con[v] = set()
    con[v].add(u)
for k, v in con.items():
    print(k, v)
