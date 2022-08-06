# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_h
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
MOD = 10**9+7
n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
tag = 'atcoder'
d = len(tag)
dp = [[0]*n for _ in range(len(tag))]
for i in range(n):
    if tag[0] == s[i]:
        dp[0][i] = 1
for i in range(d):
    for j in range(1, n):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD
        if i < d-1 and tag[i+1] == s[j]:
            dp[i+1][j] += dp[i][j-1]
            dp[i+1][j] %= MOD
    # print(i, *dp[i])
print(dp[d-1][n-1])
