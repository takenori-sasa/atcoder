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
n, m = [int(char) for char in stdin.readline().rstrip().split()]
x = [int(char) for char in stdin.readline().rstrip().split()]
bonus = {}
for _ in range(m):
    c, y = [int(char) for char in stdin.readline().rstrip().split()]
    bonus[c] = y
s = [0]*(n+1)
for i in range(n):
    zero = max(s)
    # for j in range(i+1, 0, -1):
    #     s[j] = s[j-1]+x[i]
    # print(i, x[i], s)
    for j in range(i+1, 0, -1):
        if j in bonus:
            s[j] = max(bonus[j]+s[j-1]+x[i], s[j])
        else:
            s[j] = max(s[j-1]+x[i], s[j])
    s[0] = zero
    # print('bonused', i, x[i], s)
print(max(s))
