# -*- coding: utf-8 -*-
from sys import stdin
import copy
'''
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(s) for s in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''

s = stdin.readline().rstrip()
words = ['dream', 'dreamer', 'erase', 'eraser']
tt = copy.deepcopy(words)
ans = 'NO'
while len(tt) > 0:
    prevs = copy.deepcopy(tt)
    tt = []
    for prev in prevs:
        for word in words:
            concats = prev+word
            if concats == s:
                # print(concats, s)
                ans = 'YES'
                break
            elif len(concats) <= len(s) and s.startswith(concats):
                tt.append(concats)
print(ans)
