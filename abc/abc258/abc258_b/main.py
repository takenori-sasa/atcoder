# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc258/tasks/abc258_b
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''


def concat(s, x, y, l):
    # print(s, len(s), x, y)
    if len(s) < n:
        for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            # print('move', s, len(s), x, y)
            concat(s+area[(x+dx) % n][(y+dy) % n], (x+dx) % n, (y+dy) % n, l)
    else:
        # print('end', s, type(s))
        l.add(s)
        # print(l)
        return


n = int(stdin.readline().rstrip())
area = a = [[c for c in stdin.readline().rstrip()]
            for _ in range(n)]
# print(n, area, type(area[0][0]))
ans = 0
l = set()
for i in range(n):
    for j in range(n):
        concat(area[i][j], i, j, l)
        print(len(l))
print(max(l))
# print(ans, t)
# ans = max(ans, target)
