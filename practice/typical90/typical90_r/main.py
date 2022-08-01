# -*- coding: utf-8 -*-
from sys import stdin
import math
'''
https://atcoder.jp/contests/typical90/tasks/typical90_r
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
t = int(stdin.readline().rstrip())
l, x, y = [int(char) for char in stdin.readline().rstrip().split()]
q = int(stdin.readline().rstrip())
for _ in range(q):
    e = int(stdin.readline().rstrip())
    ang = 2*math.pi*e/t
    ey, ez = -math.sin(ang), l/2-math.cos(ang)*l/2
    hori = [x, y-ey, ez]
    dist = math.sqrt(x**2+(y-ey)**2)
    dep = math.atan2(ez, dist)

    print(math.degrees(dep))
