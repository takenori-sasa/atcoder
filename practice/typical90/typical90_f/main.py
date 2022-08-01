# -*- coding: utf-8 -*-
from sys import stdin
import bisect
'''
https://atcoder.jp/contests/typical90/tasks/typical90_f
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
s = stdin.readline().rstrip()
ans = list(s[:k])
print(ans)
for i in range(k-1, n):
    if ans[-1] > s[i]:
        ans[-1] = s[i]
    else:
        ans[bisect.bisect_left(ans, s[i])] = s[i]
    print(i, ans)
