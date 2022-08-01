# -*- coding: utf-8 -*-
from sys import stdin
import itertools
'''
https://atcoder.jp/contests/typical90/tasks/typical90_af
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b, c = [int(char) for char in stdin.readline().rstrip().split()]
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip()] for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()] for _ in range(n)]
print(*ans, sep="\n")
'''
INF = float('inf')
n = int(stdin.readline().rstrip())
a = [[int(char) for char in stdin.readline().rstrip().split()]
     for _ in range(n)]
m = int(stdin.readline().rstrip())
hate = {}
for _ in range(m):
    x, y = [int(char) for char in stdin.readline().rstrip().split()]
    x, y = x-1, y-1
    if x not in hate:
        hate[x] = []
    if y not in hate:
        hate[y] = []
    hate[x].append(y)
    hate[y].append(x)
per_list = list(itertools.permutations(range(n)))
ans = INF
for p in per_list:
    cost = 0
    # print(p)
    for i in range(n):
        cost += a[p[i]][i]
        if i < n-1 and (p[i] in hate and p[i+1] in hate[p[i]]):
            cost = INF
            # print('break', i)
            break
    # print(ans, cost)
    ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)
