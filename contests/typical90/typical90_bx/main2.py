# -*- coding: utf-8 -*-
from sys import stdin
import bisect
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bx
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
wh = sum(a)
a *= 2
b = [a[0]]
for i in range(1, len(a)):
    b.append(b[-1]+a[i])
if wh % 10 != 0:
    print('No')
    exit()
tenth = wh//10
for i in range(n):
    j = bisect.bisect_left(b, tenth+b[i])
    if b[j]-b[i] == tenth:
        print('Yes')
        exit()

print('No')
