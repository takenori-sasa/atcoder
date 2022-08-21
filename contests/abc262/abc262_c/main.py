# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc262/tasks/abc262_c
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
corr = set()
inc = {}
for i in range(n):
    if a[i] == i+1:
        corr.add(a[i])
    else:
        inc[i+1] = a[i]
# print(*corr, inc)
ans = 0
for k, v in inc.items():
    if v in inc and inc[v] == k and inc[v] < inc[k]:
        ans += 1
num = len(corr)
ans += num*(num-1)//2
print(ans)
