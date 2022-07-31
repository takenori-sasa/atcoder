# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc262/tasks/abc262_b
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
n, m = [int(char) for char in stdin.readline().rstrip().split()]
con = {}
for _ in range(m):
    u, v = [int(char) for char in stdin.readline().rstrip().split()]
    if u not in con:
        con[u] = set()
    con[u].add(v)
    if v not in con:
        con[v] = set()
    con[v].add(u)
ans = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        for c in range(b+1, n+1):
            if b not in con[a] or c not in con[b] or a not in con[c]:
                continue
            elif b in con[a] and c in con[b] and a in con[c]:
                ans += 1
print(ans)
