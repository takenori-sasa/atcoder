# -*- coding: utf-8 -*-
from sys import stdin
'''
https://atcoder.jp/contests/typical90/tasks/typical90_cf
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
s = stdin.readline().rstrip()
length = [0]
binary = {'o': 1, 'x': -1}
for i in range(len(s)):
    if binary[s[i]]*length[-1] < 0:
        length.append(binary[s[i]])
    else:
        length[-1] += binary[s[i]]
ans = 0
rest = n
for i in range(len(length)):
    rest -= abs(length[i])
    ans += rest*abs(length[i])

print(ans)
