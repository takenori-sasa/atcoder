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
l = list(stdin.readline().rstrip())
ans = 0
for s in l:
    if s == '1':
        ans += 1
print(ans)
