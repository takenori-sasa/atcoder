# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc258/tasks/abc258_d
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n, x = [int(char) for char in stdin.readline().rstrip().split()]
xy = [map(int, input().split()) for _ in range(n)]
movie, clear = [list(i) for i in zip(*xy)]
ans = float('inf')
init = 0
min_clear = clear[0]
for i in range(n):
    x -= 1
    init += clear[i]+movie[i]
    time = init
    min_clear = min(clear[i], min_clear)
    rest = x

    time += min_clear*rest
    # print(init, x, time)
    ans = min(ans, time)
print(ans)
