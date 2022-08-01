# -*- coding: utf-8 -*-
from sys import stdin
from math import gcd
'''
https://atcoder.jp/contests/typical90/tasks/typical90_al
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
a, b = [int(char) for char in stdin.readline().rstrip().split()]
lcm = a*b//gcd(a, b)
if lcm > 10**18:
    print('Large')
else:
    print(lcm)
