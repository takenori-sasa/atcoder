# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_e
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
n, b, k = [int(char) for char in stdin.readline().rstrip().split()]
c = [int(char) for char in stdin.readline().rstrip().split()]
MOD = 10**9+7
dp = [[0]*b for _ in range(n)]
for i in range(k):
    dp[0][c[i] % b] += 1
# print(dp)
for i in range(1, n):
    for j in range(b):
        if dp[i-1][j] == 0:
            continue
        for digit in c:
            dp[i][(j*10+digit) % b] += dp[i-1][j]
            dp[i][(j*10+digit) % b] %= MOD
        # print(dp[i], i, j)
print(dp[n-1][0])
# print(*dp, sep="\n")
