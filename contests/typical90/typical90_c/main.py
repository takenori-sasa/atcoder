# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_c
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


def dfs(v, stack, dist):
    for g in graph[v]:
        if g not in dist:
            stack.append(g)
            dist[g] = dist[v]+1
    # print(v, stack, dist)
    if len(stack) == 0:
        return
    dfs(stack[0], stack[1:], dist)


n = int(stdin.readline().rstrip())
graph = {}
for i in range(n-1):
    a, b = [int(char) for char in stdin.readline().rstrip().split()]
    a -= 1
    b -= 1
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
dist0 = {0: 0}
# print(graph, sep="\n")
dfs(0, [], dist0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
dist = {mv: 0}
dfs(mv, [], dist)
print(max(dist.values())+1)
