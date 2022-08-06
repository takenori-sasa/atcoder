# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_l
s = stdin.readline().rstrip()
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


class Union_find:

    def __init__(self, N):
        self.par = [-1] * (N+1)
        self.siz = [1] * (N+1)

    def root(self, x):
        if self.par[x] == -1:
            # root
            return x

        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        else:
            if self.siz[x] < self.siz[y]:
                x, y = y, x

            self.par[y] = x
            self.siz[x] += self.siz[y]

            return True

    def get_size(self, x):
        return self.siz[self.root(x)]


H, W = map(int, input().split())
Q = int(input())
G = Union_find(H*W+1)
M = [-1] * (H*W+1)


def check(n, x):
    if M[x] == 1 and M[n] == 1:
        G.unite(n, x)
    return


for i in range(Q):
    A = list(map(int, input().split()))
    if A[0] == 1:
        n = W * (A[1] - 1) + (A[2] - 1)
        M[n] = 1

        if n - W >= 0:
            check(n, n - W)
        if n + W < H*W:
            check(n, n + W)
        if n % W != 0 and n - 1 >= 0:
            check(n, n - 1)
        if (n + 1) % W != 0 and n + 1 < H*W:
            check(n, n + 1)

    else:
        n1 = W * (A[1] - 1) + (A[2] - 1)
        n2 = W * (A[3] - 1) + (A[4] - 1)

        if G.issame(n1, n2) and M[n1] == 1 and M[n2] == 1:
            print("Yes")

        else:
            print("No")
