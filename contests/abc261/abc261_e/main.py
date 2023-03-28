# -*- coding: utf-8 -*-
from sys import stdin
'''
URL
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * N
for i in range(30):
    cur = C >> i & 1
    print(cur)
    f = [0, 1]
    for j, (T, A) in enumerate(TA):
        a = A >> i & 1
        if T == 1:
            f = [f[0] & a, f[1] & a]
        elif T == 2:
            f = [f[0] | a, f[1] | a]
        else:
            f = [f[0] ^ a, f[1] ^ a]
        cur = f[cur]
        ans[j] |= cur << i
