# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_d
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
h, w = [int(char) for char in stdin.readline().rstrip().split()]
data = [[int(char) for char in stdin.readline().rstrip().split()]
        for _ in range(h)]
sum_h = [sum(d) for d in data]

sum_w = [sum(d) for d in map(list, zip(*data))]
# print(sum_w, sum_h)
ans = []
for i in range(h):
    ww = []
    for j in range(w):
        ww.append(str(sum_h[i]+sum_w[j]-data[i][j]))
    print(' '.join(ww))
