# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_j
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
p1 = [0]
p2 = [0]
for _ in range(n):
    c, p = [int(char) for char in stdin.readline().rstrip().split()]
    if c == 1:
        p2.append(p2[-1])
        p1.append(p1[-1]+p)
    else:
        p1.append(p1[-1])
        p2.append(p2[-1]+p)
q = int(stdin.readline().rstrip())
for _ in range(q):
    l, r = [int(char) for char in stdin.readline().rstrip().split()]
    print(p1[r]-p1[l-1], p2[r]-p2[l-1])
