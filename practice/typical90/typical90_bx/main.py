# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bx
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
n = int(stdin.readline().rstrip())
a = [int(char) for char in stdin.readline().rstrip().split()]
wh = sum(a)
a *= 2
# print(len(a))
left = 0
right = 1
s = a[0]
ans = 'No'
while left < right and left < n:
    while s*10 < wh and right < 2*n:
        s += a[right]
        right += 1
    if s*10 == wh:
        ans = 'Yes'
        # print('up!', left, right, s)
        break
    # print('up', left, right, s)
    while s*10 > wh and left < right:
        s -= a[left]
        left += 1
    if s != 0 and s*10 == wh:
        ans = 'Yes'
        # print('down!', left, right, s)
        break
    # print('down', left, right, s)
    if left == right and left+1 < 2*n:
        right = left+1
        s += a[right]
print(ans)
