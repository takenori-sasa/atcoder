# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc264/tasks/abc264_d
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
    t = 'atcoder'
    n = len(t)
    idx = {t[i]: i for i in range(len(t))}
    sdx = {s[i]: i for i in range(len(s))}
    q = {0: set([s])}
    exist = set([s])
    if s == t:
        print(0)
        return
    cnt = 0
    while True:
        q[cnt+1] = set()
        for c in q[cnt]:
            for i in range(len(c)-1):
                cl = list(c)
                cl[i], cl[i+1] = cl[i+1], cl[i]
                u = ''.join(cl)
                if u == t:
                    print(cnt+1)
                    return
                elif u in exist:
                    continue
                exist.add(u)
                q[cnt+1].add(u)
        cnt += 1
        print(cnt, len(exist))


if __name__ == '__main__':
    main()
