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
    # s = list(int(c) for c in input())
    cnt = 0
    # first = {}
    # end = {}
    # for i in range(n):
    #     if s[i] not in first:
    #         first[s[i]] = i
    #     end[s[i]] = i
    # print(first)
    # print(end)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                idx = s.find(str(i))
                if idx == -1:
                    continue
                jdx = s.find(str(j), idx+1)
                if jdx == -1:
                    continue
                kdx = s.find(str(k), jdx+1)
                if kdx == -1:
                    continue
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
