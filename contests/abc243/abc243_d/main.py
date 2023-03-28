# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/abc243/tasks/abc243_d
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
n, x = [int(char) for char in stdin.readline().rstrip().split()]
s = stdin.readline().rstrip()


t = ['']
for c in s:
    if c == 'U':
        x >> 1
    elif c == 'R':
        x << 1
        x ^= 1
    else:
        x << 1
    print(x)
print(x)
# x = list(bin(x))
# print(''.join(x))
# for i in range(len(s)):
#     if s[i] == 'U':
#         x.pop()
#     elif s[i] == 'R':
#         x.append('1')
#     elif s[i] == 'L':
#         x.append('0')
#     print(i+1, ''.join(x), s[i])
# print(int(''.join(x), 2))
