# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bi
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
q = int(stdin.readline().rstrip())
deck = deque([])
for _ in range(q):
    t, x = [int(char) for char in stdin.readline().rstrip().split()]
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])
