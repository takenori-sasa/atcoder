# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc243/tasks/abc243_b
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n = int(stdin.readline().rstrip())
a = [int(char) for char in stdin.readline().rstrip().split()]
b = [int(char) for char in stdin.readline().rstrip().split()]
cord = {}
for i in range(len(a)):
    cord[a[i]] = i
hit = 0
blow = 0
for i in range(len(b)):
    if b[i] in cord:
        if i == cord[b[i]]:
            hit += 1
        else:
            blow += 1
print(hit)
print(blow)
