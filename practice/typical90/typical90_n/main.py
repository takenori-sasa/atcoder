# -*- coding: utf-8 -*-
from sys import stdin
from bisect import bisect_left
'''
https://atcoder.jp/contests/typical90/tasks/typical90_n
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
n = int(stdin.readline().rstrip())
a = [int(char) for char in stdin.readline().rstrip().split()]
b = [int(char) for char in stdin.readline().rstrip().split()]
# print(a, b)
a.sort()
b.sort()
ans = 0
for i in range(n):
    ans += abs(a[i]-b[i])
print(ans)
