# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_i
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
import math
n = int(stdin.readline().rstrip())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
ans = float('inf')
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            cos = (x[i]-x[j])*(x[k]-x[j])+(y[i]-y[j])*(y[k]-y[j])
            cos /= ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
            cos /= ((x[k]-x[j])**2+(y[k]-y[j])**2)**(1/2)
            ans = min(ans, cos)

print(math.degrees(math.acos(ans)))
