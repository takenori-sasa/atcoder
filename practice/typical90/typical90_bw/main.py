# -*- coding: utf-8 -*-
from sys import stdin
import math
'''
https://atcoder.jp/contests/typical90/tasks/typical90_bw
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
n = int(stdin.readline().rstrip())
num = 0
ele = {}
prime = [i+1 for i in range(1, int(math.sqrt(n))+1)]
time = 0
for p in prime:
    while n % p == 0:
        n //= p
        num += 1
if n != 1:
    num += 1
print(math.ceil(math.log2(num)))
