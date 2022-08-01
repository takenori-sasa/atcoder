# -*- coding: utf-8 -*-
from sys import stdin
import itertools
import math
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bc
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
n, p, q = [int(char) for char in stdin.readline().rstrip().split()]
a = [int(char) % p for char in stdin.readline().rstrip().split()]
ans = 0
for a1, a2, a3, a4, a5 in itertools.combinations(a, 5):
    if a1*a2 % p*a3 % p*a4 % p*a5 % p == q:
        ans += 1
print(ans)
