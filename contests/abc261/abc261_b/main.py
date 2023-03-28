# -*- coding: utf-8 -*-
from sys import stdin
'''
URL
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n = int(stdin.readline().rstrip())
data = [list(stdin.readline().rstrip()) for _ in range(n)]
ans = 'correct'
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif data[i][j] == 'D' and data[j][i] != 'D':
            ans = 'incorrect'
            break
        elif data[i][j] == 'W' and data[j][i] != 'L':
            ans = 'incorrect'
            break
        elif data[i][j] == 'L' and data[j][i] != 'W':
            ans = 'incorrect'
            break
print(ans)
