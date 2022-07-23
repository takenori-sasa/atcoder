# -*- coding: utf-8 -*-
from sys import stdin
# s = stdin.readline().rstrip()
# a = int(stdin.readline().rstrip())
# 複数行
# n = int(stdin.readline().rstrip())
# data = [stdin.readline().rstrip().split() for _ in range(n)]
a = int(stdin.readline().rstrip())
b, c = [int(s) for s in stdin.readline().rstrip().split()]
s = stdin.readline().rstrip()
print(a+b+c, s)
