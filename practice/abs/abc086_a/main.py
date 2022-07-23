# -*- coding: utf-8 -*-
from sys import stdin
# s = stdin.readline().rstrip()
# a = int(stdin.readline().rstrip())
# 複数行
# n = int(stdin.readline().rstrip())
# data = [stdin.readline().rstrip().split() for _ in range(n)]
a, b = [int(s) for s in stdin.readline().rstrip().split()]
if a % 2 == 1 and b % 2 == 1:
    print('Odd')
else:
    print('Even')
