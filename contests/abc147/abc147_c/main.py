# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
from itertools import permutations, combinations
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc147/tasks/abc147_c
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
    talks = []
    for i in range(n):
        a = int(input())
        talk = {0: set(), 1: set()}
        for j in range(a):
            x, y = [int(char) for char in input().split()]
            talk[y].add(x-1)
        talks.append(talk)
    # print(talks)
    ans = 0
    for honests in bifull(range(n)):
        liars = set(range(n)) - honests
        # print('start', honests, liars)
        is_fact = True
        for j in range(n):
            talk = talks[j]
            if j not in honests:
                continue
            # print(j, talk[1], talk[0])
            for honest in talk[1]:
                if honest in liars:
                    is_fact = False
            for liar in talk[0]:
                if liar in honests:
                    is_fact = False
        if is_fact:
            # print('fact', honests, liars)
            ans = max(ans, len(honests))
    print(ans)


def bifull(__bilist__):
    _num_ = len(__bilist__)
    _ret_ = []
    for k in range(_num_+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(set(comb))
    return _ret_


if __name__ == '__main__':
    main()
