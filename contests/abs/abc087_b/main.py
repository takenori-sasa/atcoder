# -*- coding: utf-8 -*-
from sys import stdin
'''
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(s) for s in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
x = int(stdin.readline().rstrip())
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*i+100*j+50*k == x:
                ans += 1
print(ans)
