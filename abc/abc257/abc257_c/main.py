# -*- coding: utf-8 -*-
from sys import stdin
from statistics import mean
'''
https://atcoder.jp/contests/abc257/tasks/abc257_c
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
if len(set(s)) == 1:
    print(n)
    exit()
kids = set()
adults = set()
for i in range(n):
    if s[i] == '0':
        kids.add(i)
    else:
        adults.add(i)
w = [int(c) for c in stdin.readline().rstrip().split()]
rest = set([i for i in range(n)])
ans = 0
weight = {}
for i in range(n):
    weight[i] = w[i]
# print(weight)
border = mean(w)
while True:
    upper = set()
    lower = set()
    for r in rest:
        if weight[r] < border:
            lower.add(r)
        else:
            upper.add(r)
    if len(lower & kids) < len(upper & adults):
        rest = lower
    elif len(lower & kids) > len(upper & adults):
        rest = upper
    else:
        break
    border = mean([weight[r] for r in rest])
# print(border)
upper = set()
lower = set()
for r in rest:
    if weight[r] < border:
        lower.add(r)
    else:
        upper.add(r)
print(len(lower & kids) + len(upper & adults))
