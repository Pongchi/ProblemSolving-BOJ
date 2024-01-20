# https://www.acmicpc.net/problem/14003

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))
lis = [seq[0]]

for i in range(1, A):
    if lis[-1] < seq[i]:
        lis.append(seq[i])
    else:
        idx = bisect_left(lis, seq[i])
        lis[idx] = seq[i]
