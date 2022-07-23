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
n, c = [int(char) for char in stdin.readline().rstrip().split()]
seq = []
for _ in range(n):
    seq.append([int(char) for char in stdin.readline().rstrip().split()])
multiplier = [seq[0][1]]
for i in range(n-1):
    e = multiplier[-1]
    if seq[i][0] == 1:
        e &= seq[i][1]
    elif seq[i][0] == 2:
        e |= seq[i][1]
    elif seq[i][0] == 3:
        e ^= seq[i][1]
    multiplier.append(e)


ans = c
for i in range(n):
    if seq[0][0] == 1:
        ans &= multiplier[i]
    elif seq[0][0] == 2:
        ans |= multiplier[i]
    elif seq[0][0] == 3:
        ans ^= multiplier[i]
    print(ans)
print(multiplier)
