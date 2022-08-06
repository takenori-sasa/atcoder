# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_ab
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
n = int(stdin.readline().rstrip())
LENGTH = 1000
imos = [[0]*LENGTH for _ in range(LENGTH)]
for _ in range(n):
    lx, ly, rx, ry = [int(char) for char in stdin.readline().rstrip().split()]
    lx, ly, rx, ry = lx-1, ly-1, rx-1, ry-1
    imos[rx][ry] -= 1
    imos[lx][ly] -= 1
    imos[lx][ry] += 1
    imos[rx][ly] += 1
# print(*imos)
for i in range(LENGTH-1):
    for j in range(LENGTH-1):
        imos[i][j+1] += imos[i][j]
for i in range(LENGTH-1):
    for j in range(LENGTH-1):
        imos[i+1][j] += imos[i][j]
ans = [0]*(n+1)
for i in range(LENGTH):
    for j in range(LENGTH):
        ans[imos[i][j]] += 1
for i in range(n, 0, -1):
    print(ans[i])
