# -*- coding: utf-8 -*-
from sys import stdin
'''
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(c) for c in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
s = stdin.readline().rstrip()
a = [int(s) for s in stdin.readline().rstrip().split()]
a = sorted(a, reverse=True)
alice = 0
bob = 0
for i in range(len(a)):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]
print(alice-bob)
