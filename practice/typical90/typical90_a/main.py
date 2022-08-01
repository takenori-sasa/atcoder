# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_a
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
n, l = [int(char) for char in stdin.readline().rstrip().split()]
k = int(stdin.readline().rstrip())
a = [int(char) for char in stdin.readline().rstrip().split()]
left = 1
right = l
time = 0
while left+1 < right:
    half = (left+right)//2
    print('start', time, left, right, half)
    num_piece = 1
    last = 0
    for i in range(n):
        if a[i]-last >= half and l-a[i] >= half:
            num_piece += 1
            last = a[i]
            print('cut', i, a[i])
    # if l-last >= half:
    #     num_piece += 1
    #     print('can cut')
    if num_piece >= k+1:
        left = half
    else:
        right = half
    print('end', time, num_piece)
    time += 1
print(left)
