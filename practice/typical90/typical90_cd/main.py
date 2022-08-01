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
l_l, l_r = len(str(l)), len(str(r))
ans = 0
MOD = 10**9+7
if l_l == l_r:
    ans = (r % MOD-l % MOD+1)*(l % MOD+r % MOD) % MOD//2
if l_l+1 == l_r:
    ans += (l % MOD+(10**l_l-1) % MOD)*((10**l_l-1) % MOD-l % MOD) % MOD//2
    ans += (r % MOD+(10**l_r) % MOD)*((r+1) %
                                      MOD - (10**(l_r-1)) % MOD+1) % MOD//2
    # for i in range(l, r+1):
    #     length = len(str(i)) % MOD
    #     length *= i % MOD
    #     length %= MOD
    #     ans += length
    #     ans %= MOD
print(ans)
