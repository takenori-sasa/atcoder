# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_at
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
b = [int(char) for char in stdin.readline().rstrip().split()]
c = [int(char) for char in stdin.readline().rstrip().split()]
MOD = 46
r_a = {i: 0 for i in range(MOD)}
r_b = {i: 0 for i in range(MOD)}
r_c = {i: 0 for i in range(MOD)}
for i in range(n):
    r_a[a[i] % MOD] += 1
    r_b[b[i] % MOD] += 1
    r_c[c[i] % MOD] += 1
# print(r_a)
new_a = {i: 0 for i in range(MOD)}
for i in range(MOD):
    for j in range(MOD):
        new_a[(i+j) % MOD] += r_b[j]*r_a[i]
# print(new_a)
nn_a = {i: 0 for i in range(MOD)}

for i in range(MOD):
    for j in range(MOD):
        nn_a[(i+j) % MOD] += r_c[j]*new_a[i]
print(nn_a[0])
