# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_z
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


def dfs(v, pm):
    if v not in color:
        color[v] = pm
    else:
        for nv in graph[v]:
            if nv in color:
                continue
            else:
                dfs(nv, -pm)


n = int(stdin.readline().rstrip())
graph = {}
for _ in range(n-1):
    a, b = [int(char) for char in stdin.readline().rstrip().split()]
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)
    if b not in graph:
        graph[b] = set()
    graph[b].add(a)
# print(graph)
color = {}
dfs(list(graph.keys())[0], 1)
# print(color)
black = []
white = []
for k, v in color.items():
    if v == 1:
        black.append(str(k))
    else:
        white.append(str(k))
if len(black) > len(white):
    print(*black[:n//2])
else:
    print(*white[:n//2])
