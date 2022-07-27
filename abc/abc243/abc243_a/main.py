# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc243/tasks/abc243_a
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
v, a, b, c = [int(char) for char in stdin.readline().rstrip().split()]
ans = ''
while True:
    if v < a:
        ans = 'F'
        break
    else:
        v -= a
    if v < b:
        ans = 'M'
        break
    else:
        v -= b
    if v < c:
        ans = 'T'
        break
    else:
        v -= c
print(ans)
