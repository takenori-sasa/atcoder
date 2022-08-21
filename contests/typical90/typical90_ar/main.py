# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_ar
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
N, Q = [int(char) for char in stdin.readline().rstrip().split()]
A = {i: int(c) for i, c in enumerate(stdin.readline().rstrip().split())}
idx = 0
# print(A)
for _ in range(Q):
    t, x, y = [int(char) for char in stdin.readline().rstrip().split()]
    if t == 1:
        # print('change', A[(x-1-idx) % N], A[(y-1-idx) % N])
        A[(x-1-idx) % N], A[(y-1-idx) % N] = A[(y-1-idx) % N], A[(x-1-idx) % N]
    elif t == 2:
        idx = (idx+1) % N
        # print(idx)
    else:
        print(A[(-idx+x-1) % N])
