# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_ca
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
h, w = [int(char) for char in stdin.readline().rstrip().split()]
a = [[int(char) for char in stdin.readline().rstrip().split()]
     for _ in range(h)]
b = [[int(char) for char in stdin.readline().rstrip().split()]
     for _ in range(h)]
c = [[a[i][j]-b[i][j] for j in range(w)] for i in range(h)]
ans = 0
for i in range(h-1):
    for j in range(w-1):
        diff = c[i][j]
        ans += abs(diff)
        c[i][j] = 0
        c[i][j+1] -= diff
        c[i+1][j] -= diff
        c[i+1][j+1] -= diff
    if c[i][w-1] != 0:
        print('No')
        exit()
    # print(*c, sep="\n")
for j in range(w):
    if c[h-1][j] != 0:
        print('No')
        exit()
print('Yes')
print(ans)
