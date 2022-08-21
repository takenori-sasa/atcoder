# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc259/tasks/abc259_c
s = stdin.readline().rstrip()
b, c = [int(char) for char in input().split()]
a = [int(char) for char in input().split()]
n = int(input().rstrip())
for _ in range(n):
    a = [int(char) for char in input().split()]
data = [input().split() for _ in range(n)]
data = [[int(char) for char in input().split()] for _ in range(n)]
data = [[int(char) for char in input().split()] for _ in range(n)]
print(*ans, sep="\n")
転置
trans=map(list, zip(*data))
'''
# INF = float('inf')
# MOD = 10**9+7


def main():

    s = input().rstrip()
    t = input().rstrip()
    rlet = []
    target = t[0]
    cnt = 1
    for i in range(1, len(t)):
        c = t[i]
        if target == c:
            cnt += 1
        else:
            rlet.append((target, cnt))
            cnt = 1
            target = c
    rlet.append((target, cnt))
    rles = []
    target = s[0]
    cnt = 1
    for i in range(1, len(t)):
        c = t[i]
        if target == c:
            cnt += 1
        else:
            rles.append((target, cnt))
            cnt = 1
            target = c
    rles.append((target, cnt))
    ans = 'Yes'
    if len(rles) != len(rlet):
        ans = 'No'
    else:
        for i in range(len(rles)):
            if rles[i][0] != rlet[i][0]
            ans = 'No'
            elif rles[i][1] < rlet[i][] and rlet[i][1]
        print('Yes')


if __name__ == '__main__':
    main()
