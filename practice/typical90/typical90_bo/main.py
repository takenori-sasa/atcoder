# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bo
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


def base10int(value, base):
    if (value // base):
        return base10int(value // base, base) + str(value % base)
    return str(value % base)


n, k = [char for char in stdin.readline().rstrip().split()]
k = int(k)
for _ in range(k):
    tenth = int(n, 8)
    ninth = base10int(tenth, 9)
    n = ''
    for i in range(len(ninth)):
        if ninth[i] == '8':
            n += '5'
        else:
            n += ninth[i]
print(n)
