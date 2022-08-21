# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bz
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
graph = {}
for _ in range(m):
    a, b = [int(char) for char in stdin.readline().rstrip().split()]
    if a not in graph:
        graph[a] = set()
    if a > b:
        graph[a].add(b)
    if b not in graph:
        graph[b] = set()
    if a < b:
        graph[b].add(a)
ans = 0
for i in range(1, n+1):
    if i in graph and len(graph[i]) == 1:
        ans += 1
print(ans)
