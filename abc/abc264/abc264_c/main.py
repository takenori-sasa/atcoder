# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left
import math
sys.setrecursionlimit(10**9)
'''
https://atcoder.jp/contests/abc264/tasks/abc264_c
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
    ha, wa = [int(char) for char in input().split()]
    ma = [[int(char) for char in input().split()] for _ in range(ha)]
    hb, wb = [int(char) for char in input().split()]
    mb = [[int(char) for char in input().split()] for _ in range(hb)]
    # print(*ma)
    tmp = []
    j = 0
    for i in range(hb):
        while j < ha:
            # print(i, mb[i], j, ma[j], set(mb[i]) <= set(ma[j]))
            if set(mb[i]) <= set(ma[j]):
                tmp.append(ma[j])
                j += 1
                break
            j += 1
    # print(*tmp)
    if len(tmp) < hb:
        print('No')
        exit()
    tmp = [list(x) for x in zip(*tmp)]
    mb = [list(x) for x in zip(*mb)]
    ans = []
    j = 0
    for i in range(wb):
        while j < wa:
            if set(mb[i]) <= set(tmp[j]):
                ans.append(tmp[j])
                j += 1
                break
            j += 1
    out = 'Yes'
    # print(*ans)
    if len(ans) < wb:
        print('No')
        exit()
    for i in range(hb):
        if ans[i] != mb[i]:
            out = 'No'
            break
    print(out)


if __name__ == '__main__':
    main()
