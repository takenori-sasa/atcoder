# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_p
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
a, b, c = [int(char) for char in stdin.readline().rstrip().split()]
ans = 9999
for i in range(ans):
    for j in range(ans-i):
        sum_k = n-a*i-b*j
        if sum_k < 0:
            continue
        if sum_k % c == 0:
            k = sum_k//c
            ans = min(ans, i+j+k)
print(ans)
