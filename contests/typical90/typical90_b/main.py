# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_b
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


def dfs(s, left, right):
    # print(s, left, right)
    if left > right:
        # print('out', s)
        #     exit()
        # elif left == right:
        #     print(s)
        #     exit()
        return
    if left == 0 and right == 0:
        print(s)
    if left > 0:
        dfs(s+'(', left-1, right)
    if right > 0:
        dfs(s+')', left, right-1)


n = int(stdin.readline().rstrip())
if n % 2 == 1:
    print('')
    exit()
left = n//2-1
right = n//2
dfs('(', left, right)
