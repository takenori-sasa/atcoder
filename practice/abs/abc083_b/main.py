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
n, a, b = [int(s) for s in stdin.readline().rstrip().split()]
ans = 0
for i in range(1, n+1):
    s = sum([int(c) for c in list(str(i))])
    if s >= a and s <= b:
        ans += i
print(ans)
