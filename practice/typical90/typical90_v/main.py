# -*- coding: utf-8 -*-
from sys import stdin
from math import gcd

'''
https://atcoder.jp/contests/typical90/tasks/typical90_v
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
a, b, c = [int(char) for char in stdin.readline().rstrip().split()]
r = gcd(a, gcd(b, c))
# print(r)
ans = 0
ans += a//r-1
ans += b//r-1
ans += c//r-1
print(ans)
