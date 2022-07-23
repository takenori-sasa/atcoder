# -*- coding: utf-8 -*-
from sys import stdin
'''
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(s) for s in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n = int(stdin.readline().rstrip())
d = set()
for _ in range(n):
    d.add(int(stdin.readline().rstrip()))
print(len(d))
