# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc054/tasks/abc054_c
import sys
from bisect import bisect_left, bisect_right
import math
from itertools import permutations, combinations
INF = float('inf')
MOD = 10**9+7
'''
    s,t = list(map(str, input().split()))
    field = [''.join(input().split()) for _ in range(n)]
'''


def main():
    n, m = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(m)]
    graph = {}
    for a, b in grid:
        a, b = a-1, b-1
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    cnt = 0
    for perm in permfull(range(n)):
        temp = perm[0]
        if temp != 0:
            continue
        visited = set([temp])
        # print(perm)
        onelen = True
        for v in perm[1:]:
            # print(v, visited)
            if v not in graph[temp] or v in visited:
                onelen = False
                # print('not')
                break
            else:
                temp = v
                visited.add(v)
        if onelen:
            # print('onelen')
            cnt += 1
    print(cnt)


'''
    for _ in range(n):
        a = [int(char) for char in input().split()]
    print(*ans, sep="\n")
    trans=map(list, zip(*data))
'''


def bifull(__bilist__):
    _num_ = len(__bilist__)
    _ret_ = []
    for k in range(_num_+1):
        for comb in combinations(__bilist__, k):
            _ret_.append(set(comb))
    return _ret_


def accm(li):
    _ret_ = [0]
    _num_ = len(li)
    for i in range(_num_):
        _ret_.append(_ret_[-1]+li[i])
    return _ret_


def permfull(arr, num=-1):
    _num_ = len(arr)
    _ret_ = []
    if num == -1:
        num = _num_
    for perm in permutations(arr, num):
        _ret_.append(list(perm))
    return _ret_


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    main()
