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
n, y = [int(s) for s in stdin.readline().rstrip().split()]
a = -1
b = -1
c = -1
for i in range(n+1):
    for j in range(n+1):
        k = n-i-j
        if k >= 0 and 10000*i+5000*j + 1000*k == y:
            a = i
            b = j
            c = k
            break
print(a, b, c)
