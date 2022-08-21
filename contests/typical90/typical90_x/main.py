# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_x
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
n, k = [int(char) for char in stdin.readline().rstrip().split()]
a = [int(char) for char in stdin.readline().rstrip().split()]
b = [int(char) for char in stdin.readline().rstrip().split()]
for i in range(n):
    k -= abs(a[i]-b[i])
ans = 'No'
if k >= 0 and k % 2 == 0:
    ans = 'Yes'
print(ans)
