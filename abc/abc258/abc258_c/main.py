# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc258/tasks/abc258_c
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n, q = [int(char) for char in stdin.readline().rstrip().split()]
s = stdin.readline().rstrip()
queries = [[int(c) for c in stdin.readline().rstrip().split()]
           for _ in range(q)]
first_index = 0
# print(queries)
for query in queries:
    idx = query[1]
    if query[0] == 2:
        print(s[(first_index+idx-1) % n])
    else:
        first_index = (first_index-idx) % n
