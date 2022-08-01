# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bq
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
n, k = [int(char) for char in stdin.readline().rstrip().split()]
r = [(k-2) % MOD]


def ppow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= MOD
        x *= x % MOD
        n >>= 1
    return ans % MOD


if k == 1:
    if n == 1:
        print(1)
    else:
        print(0)
elif n == 1:
    print(k % MOD)
elif n == 2:
    print(k*(k-1) % MOD)
else:
    print(k*(k-1) % MOD*ppow(k-2, n-2) % MOD)
