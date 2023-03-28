# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc122/tasks/abc122_b
    for _ in range(n):
        a = [int(char) for char in input().split()]
    data = [input().split() for _ in range(n)]
    print(*ans, sep="\n")
転置
    trans=map(list, zip(*data))
'''
# INF = float('inf')
# MOD = 10**9+7


def main():
    s = input()
    leng = 0
    for i in range(10+1):
        for j in range(i+1, 10+1):
            tag = s[i:j]
            if set(list(tag)) <= set(['A', 'C', 'G', 'T']):
                leng = max(leng, len(tag))
    print(leng)


if __name__ == '__main__':
    main()
