# -*- coding: utf-8 -*-
from sys import stdin
'''
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(s) for s in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
l = stdin.readline().rstrip()
a = [int(s) for s in stdin.readline().rstrip().split()]
times = 0
# print(l, a)
flag = True
while flag:
    for i in range(len(a)):
        if a[i] % 2 == 1:
            flag = False
            break
        else:
            a[i] //= 2
    times += 1
print(times-1)
