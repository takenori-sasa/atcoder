# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
from itertools import permutations, combinations
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
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
    n = int(input())
    s = input()
    cnt = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if str(i) not in s or str(k) not in s:
                    continue
                idx_i = min([l for l in range(n) if s[l] == str(i)])
                idx_k = max([l for l in range(n) if s[l] == str(k)])
                if str(j) in s[idx_i+1:idx_k]:
                    cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
