# -*- coding: utf-8 -*-
from sys import stdin
import datetime
'''
https://atcoder.jp/contests/abc258/tasks/abc258_a
s = stdin.readline().rstrip()
a = int(stdin.readline().rstrip())
b,c = [int(char) for char in stdin.readline().rstrip().split()]
複数行
n = int(stdin.readline().rstrip())
data = [stdin.readline().rstrip().split() for _ in range(n)]
'''
k = int(stdin.readline().rstrip())
dt = datetime.datetime(2018, 2, 1, hour=21)
td = datetime.timedelta(minutes=k)
dt += td
print(dt.strftime('%H:%M'))
