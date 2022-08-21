# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_cd
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
l, r = [int(char) for char in stdin.readline().rstrip().split()]
digit_l, digit_r = len(str(l)), len(str(r))
ans = 0
MOD = 10**9+7
for digit in range(digit_l, digit_r+1):
    left = max(10**(digit-1), l)
    right = min(10**(digit)-1, r)
    tmp = (digit)*(left+right)*(right-left+1)//2 % MOD
    ans += tmp
    ans %= MOD
    print(ans, digit, left, right)
print(ans)
