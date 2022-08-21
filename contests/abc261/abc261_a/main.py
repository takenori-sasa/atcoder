# -*- coding: utf-8 -*-
from sys import stdin
'''
URL
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
l1, r1, l2, r2 = [int(char) for char in stdin.readline().rstrip().split()]
l = max(l1, l2)
r = min(r1, r2)
print(max(r-l, 0))
