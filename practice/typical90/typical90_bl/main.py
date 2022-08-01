# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bl
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b, c = [int(char) for char in stdin.readline().rstrip().split()]
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip()] for _ in range(n)]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(n)]
print(*ans, sep="\n")
'''
n, q = [int(char) for char in stdin.readline().rstrip().split()]
a = [int(char) for char in stdin.readline().rstrip().split()]
d = [a[i]-a[i+1] for i in range(n-1)]
e = sum([abs(c) for c in d])
# print(d)
for _ in range(q):
    l, r, v = [int(char) for char in stdin.readline().rstrip().split()]
    l, r = l-1, r-1
    # print(l, r)
    diff = 0
    if l > 0:
        old = abs(d[l-1])
        d[l-1] -= v
        new = abs(d[l-1])
        e += new-old
    if r < n-1:
        old = abs(d[r])
        d[r] += v
        new = abs(d[r])
        e += new-old
    print(e)
